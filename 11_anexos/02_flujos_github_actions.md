# Anexo 2: Flujos y Workflows de GitHub Actions

## 1. Arquitectura del Workflow Idempotente: `setup-issues.yml`
Este workflow resuelve de forma definitiva el problema técnico del disparo automático de tareas formativas al momento de inicializar el repositorio del estudiante (aplicable tanto en la fase inicial de GitHub Classroom como en la orquestación actual con ClassMoji):

```yaml
name: Setup Initial Classroom Issues
on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

permissions:
  contents: read
  issues: write

jobs:
  create-issues:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Verify Existing Issues (Idempotency Check)
        id: check_issues
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          COUNT=$(gh issue list --state all --json number --jq 'length')
          echo "Existing issues count: $COUNT"
          echo "count=$COUNT" >> $GITHUB_OUTPUT

      - name: Seed Formative Checklist Issues
        if: steps.check_issues.outputs.count == '0'
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          gh issue create \
            --title "Hito 1: Maquetación y Semántica Base" \
            --body "### Checklist Formativa\n- [ ] Estructura semántica en index.html\n- [ ] Inclusión de meta viewport\n- [ ] Pruebas locales ejecutadas"
          
          gh issue create \
            --title "Hito 2: Estilos Responsivos y Accesibilidad" \
            --body "### Checklist Formativa\n- [ ] Breakpoints en @media\n- [ ] Contraste verificado con WCAG AA\n- [ ] Commit y push con autograding verde"
```

---

## 2. Flujo de Autograding y Feedback en Pull Request
```yaml
name: Continuous Autograding & Feedback
on:
  pull_request:
    branches: [ main ]
  push:
    branches: [ main ]

jobs:
  test-and-grade:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Node Environment
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Dependencies
        run: npm ci

      - name: Run Test Suite
        id: run_tests
        run: npm test -- --coverage

      - name: Generate Formative Report
        if: always()
        run: |
          echo "### Reporte Formativo Automatizado" >> $GITHUB_STEP_SUMMARY
          echo "Estado de ejecución: ${{ steps.run_tests.outcome }}" >> $GITHUB_STEP_SUMMARY
```
