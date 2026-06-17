# CQM_MICRESULTS_PAR

> The CQM queue parameters table is the storage location of the secondary name/value pairs of data that are associated with a CQM transaction. This table contains information for the MDI Results application.

**Description:** MDI Results CQM Queue Parameters  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was inserted. |
| 3 | `PARAM_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the CQM queue parameters table. It is an internal system assigned number. |
| 4 | `PARAM_NAME` | VARCHAR(48) | NOT NULL |  | Name of the data element. |
| 5 | `PARAM_VALUE` | VARCHAR(255) | NOT NULL |  | This is the value of the unique primary identifier of the CQM queue table. It is an internal system assigned number. |
| 6 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the CQM queue table. It is an internal system assigned number. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUEUE_ID` | [CQM_MICRESULTS_QUE](CQM_MICRESULTS_QUE.md) | `QUEUE_ID` |

