# BB_REQS_EXCEPTION

> Contains a record of every blood bank exception that involved transfusion requirements on the patient.

**Description:** Blood Bank Requirements Exceptions  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `EXCEPTION_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the BB_EXCEPTION table. An internal system-assigned number. On this table, it corresponds to the exception that involved a patient's transfusion requirements not being met. |
| 6 | `REQS_EXCEPTION_ID` | DOUBLE | NOT NULL |  | The primary key to this table. An internal system-assigned number that makes each row unique. |
| 7 | `REQUIREMENT_CD` | DOUBLE | NOT NULL |  | The transfusion requirement that was not met during the dispense transaction with a product. |
| 8 | `SPECIAL_TESTING_CD` | DOUBLE | NOT NULL |  | The special testing attribute that should have existed on the product dispensed, in order to meet the transfusion requirement of the patient. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXCEPTION_ID` | [BB_EXCEPTION](BB_EXCEPTION.md) | `EXCEPTION_ID` |

