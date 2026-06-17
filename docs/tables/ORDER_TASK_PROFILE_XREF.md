# ORDER_TASK_PROFILE_XREF

> order_task_profile_xref

**Description:** Defines the discrete task assays that are associated with an ORC/OT relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | Foreign key from order_catalog table. |
| 2 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to order_task table. |
| 3 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Foreign key from discrete_task_assay table |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_TASK_XREF](ORDER_TASK_XREF.md) | `CATALOG_CD` |
| `CATALOG_CD` | [PROFILE_TASK_R](PROFILE_TASK_R.md) | `CATALOG_CD` |
| `REFERENCE_TASK_ID` | [ORDER_TASK_XREF](ORDER_TASK_XREF.md) | `REFERENCE_TASK_ID` |
| `TASK_ASSAY_CD` | [PROFILE_TASK_R](PROFILE_TASK_R.md) | `TASK_ASSAY_CD` |

