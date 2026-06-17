# HLA_AB_SCREEN_HISTORY_MAP

> Provides for the mapping of discrete task assay results for a specific orderable procedure to the appropriate fields in the Person HLA Antibody Screen record. This mapping is used to create these records when the results are released for charting.

**Description:** HLA Antibody Screen History Map  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `B_CELL_PRA_DTA_CD` | DOUBLE | NOT NULL | FK→ | The code specifying the discrete task assay which contains the B-Cell Panel Reactive Antibody percentage to be used in creating an Antibody Screen history record. It is a foreign key reference to the primary key of the discrete_task_assay table. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The code referencing the order catalog procedure from which the Antibody Screen history record(s) will be built. It is a foreign key reference to the primary key of the order_catalog table. |
| 3 | `DILUTION_DTA_CD` | DOUBLE | NOT NULL | FK→ | The code specifying the discrete task assay which contains the dilution to be used in creating an Antibody Screen history record. It is a foreign key reference to the primary key of the discrete_task_assay table. |
| 4 | `DILUTION_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry to use for dilution in creating an Antibody Screen history record. It is a foreign key reference to the primary key of the nomenclature table. |
| 5 | `METHODOLOGY_DTA_CD` | DOUBLE | NOT NULL | FK→ | The code specifying the discrete task assay which contains the methodology to be used in creating an Antibody Screen history record. It is a foreign key reference to the primary key of the discrete_task_assay table. |
| 6 | `METHODOLOGY_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry to use for methodology in creating an Antibody Screen history record. It is a foreign key reference to the primary key of the nomenclature table. |
| 7 | `OD_DTA_CD` | DOUBLE | NOT NULL |  | Allows the user to map a discrete task assay to the od value on the history tables for antibody screens. |
| 8 | `OD_RATIO_DTA_CD` | DOUBLE | NOT NULL |  | Allows the user to map a discrete task assay to the od ratio value on the history tables for antibody screens. |
| 9 | `REACTION_DTA_CD` | DOUBLE | NOT NULL | FK→ | The code specifying the discrete task assay which contains the reaction to be used in creating an Antibody Screen history record. It is a foreign key reference to the primary key of the discrete_task_assay table. |
| 10 | `SEQ_NUMBER` | DOUBLE | NOT NULL |  | Arbitrarily assigned number to make each record unique. This is necessary since multiple HLA Antibody Screen History Map records may be created for a single order catalog procedure. |
| 11 | `T_CELL_PRA_DTA_CD` | DOUBLE | NOT NULL | FK→ | The code specifying the discrete task assay which contains the T-Cell Panel Reactive Antibody percentage to be used in creating an Antibody Screen history record. It is a foreign key reference to the primary key of the discrete_task_assay table. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `B_CELL_PRA_DTA_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `DILUTION_DTA_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `DILUTION_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `METHODOLOGY_DTA_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `METHODOLOGY_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `REACTION_DTA_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `T_CELL_PRA_DTA_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

