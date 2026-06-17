# HLA_AB_SPEC_MAP

> Provides for the mapping of discrete task assay results for a specific orderable procedure to the appropriate fields in the Person Antibody Specificity record. This mapping is used to create these records when the results are released for charting.

**Description:** HLA Antibody Specificity Map  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AB_DTA_CD` | DOUBLE | NOT NULL | FK→ | The code specifying the discrete task assay which contains the Antibody specificity to be used in creating an Antibody Screen Specificity history record. It is a foreign key reference to the primary key of the discrete_task_assay table. |
| 2 | `AB_HIST_SEQ_NBR` | DOUBLE | NOT NULL |  | Allows the link between the hla_ab_spec_map and hla_ab_screen_history_map tables. |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The code referencing the order catalog procedure from which the Antibody Screen Specificity history record(s) will be built. It is a foreign key reference to the primary key of the order_catalog table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AB_DTA_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |

