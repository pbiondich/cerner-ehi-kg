# EI_INTERMEDHX_TRANSACTION

> This table will retain the associated transactions when retrieving the data from Medicare.

**Description:** Eligible Information - Medicare Transactions  
**Table type:** ACTIVITY  
**Primary key:** `EI_INTERMEDHX_TRANSACTION_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EI_INTERMEDHX_TRANSACTION_ID` | DOUBLE | NOT NULL | PK | The primary key of the record |
| 2 | `ERROR_MESSAGE_DETAIL` | VARCHAR(1000) |  |  | This is the value actual error message from the call to Medicare |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number |
| 4 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | This is the date time value of when the transaction was saved to the database |
| 5 | `TRANSACTION_ERROR_FLAG` | DOUBLE | NOT NULL |  | Error flag |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EI_ELIGIBLE_SERVICE](EI_ELIGIBLE_SERVICE.md) | `LAST_TRANSACTION_UPDATE_ID` |

