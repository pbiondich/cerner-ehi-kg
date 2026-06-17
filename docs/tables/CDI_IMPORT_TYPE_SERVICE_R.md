# CDI_IMPORT_TYPE_SERVICE_R

> Stores import type and service instance relationships.

**Description:** Cerner Document Imaging Import Type Service Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_IMPORT_TYPE_ID` | DOUBLE |  | FK→ | Unique number that identifies an import type. |
| 2 | `CDI_IMPORT_TYPE_SERVICE_R_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDI_IMPORT_TYPE_SERVICE_R table. |
| 3 | `CDI_SERVICE_INSTANCE_ID` | DOUBLE |  | FK→ | Unique number that identifies a service instance. |
| 4 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_IMPORT_TYPE_ID` | [CDI_IMPORT_TYPE](CDI_IMPORT_TYPE.md) | `CDI_IMPORT_TYPE_ID` |
| `CDI_SERVICE_INSTANCE_ID` | [CDI_SERVICE_INSTANCE](CDI_SERVICE_INSTANCE.md) | `CDI_SERVICE_INSTANCE_ID` |

