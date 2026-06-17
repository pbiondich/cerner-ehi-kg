# HLA_XM_HISTORY_MAP

> Provides for the mapping of discrete task assay results for a specific orderable procedure to appropriate fields in the Person HLA Crossmatch record. This mapping is used to create these records when the results are released for charting.

**Description:** HLA Crossmatch History Map  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `B_CELL_RESULT_DTA_CD` | DOUBLE | NOT NULL | FK→ | The code specifying the discrete task assay which contains the B-Cell Reactive result. It is a foreign key reference to the primary key of the discrete_task_assay table. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The code referencing the order catalog procedure from which the Crossmatch history record(s) will be built. It is a foreign key reference to the primary key of the order_catalog table. |
| 3 | `INTERPRETATION_DTA_CD` | DOUBLE | NOT NULL | FK→ | The code specifying the discrete task assay which contains the Interpretation result. It is a foreign key reference to the primary key of the discrete_task_assay table. |
| 4 | `MONO_CELL_RESULT_DTA_CD` | DOUBLE | NOT NULL | FK→ | The code specifying the discrete task assay which contains the Monocyte Cell Reactive result. It is a foreign key reference to the primary key of the discrete_task_assay table. |
| 5 | `TB_CELL_RESULT_DTA_CD` | DOUBLE | NOT NULL | FK→ | The code specifying the discrete task assay which contains the T/B-Cell Reactive result. It is a foreign key reference to the primary key of the discrete_task_assay table. |
| 6 | `T_CELL_RESULT_DTA_CD` | DOUBLE | NOT NULL | FK→ | The code specifying the discrete task assay which contains the T-Cell Reactive result. It is a foreign key reference to the primary key of the discrete_task_assay table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `XM_TYPE_DTA_CD` | DOUBLE | NOT NULL | FK→ | The code specifying the discrete task assay which contains the crossmatch type result. It is a foreign key reference to the primary key of the discrete_task_assay table. |
| 13 | `XM_TYPE_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry to use for crossmatch type in creating an crossmatch history record. It is a foreign key reference to the primary key of the nomenclature table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `B_CELL_RESULT_DTA_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `INTERPRETATION_DTA_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `MONO_CELL_RESULT_DTA_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `TB_CELL_RESULT_DTA_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `T_CELL_RESULT_DTA_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `XM_TYPE_DTA_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `XM_TYPE_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

