# EI_ELIGIBLE_SERVICE

> This table will be used to track a person's medicare eligible preventative services.

**Description:** Eligible Information - for Medicare Eligible Services  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EI_ELIGIBLE_SERVICE_ID` | DOUBLE | NOT NULL |  | The Primary Key for the record |
| 3 | `ELIGIBLE_DT_TM` | DATETIME | NOT NULL |  | This field identifies the next time the person is eligible for a given service |
| 4 | `ELIGIBLE_SRVC_CD` | DOUBLE | NOT NULL |  | The CTP code (GCODE) that is returned from Medicare and converted to a CODE VALUE |
| 5 | `FREQUENCY_OF_SERVICE_TXT` | VARCHAR(1000) |  |  | This is a text field that describes how often an eligible service can be ordered for a patient |
| 6 | `LAST_TRANSACTION_UPDATE_ID` | DOUBLE | NOT NULL | FK→ | the FK value from EI_INTERMEDHX_TRANSACTION(EI_INTERMEDHX_TRANSACTION_ID) |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of a unique primary identifier of the person table. It is an internal system assigned number. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LAST_TRANSACTION_UPDATE_ID` | [EI_INTERMEDHX_TRANSACTION](EI_INTERMEDHX_TRANSACTION.md) | `EI_INTERMEDHX_TRANSACTION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

