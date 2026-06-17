# AUTH_ERROR

> This activity table is used to track instances where a user has attempted to verify a result and attempts to reauthenticate themselves unsuccessfully three (consecutive) times. One row is written after the third consecutive incorrect attempt.

**Description:** Auth_Error  
**Table type:** ACTIVITY  
**Primary key:** `AUTH_ERROR_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | This column is used to store the number of the application the user was using when unsuccessfully attempting to re-authenticate themselves. |
| 2 | `AUTH_ERROR_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies a row on the Auth_Error table. This field would be used to join to the auth_error_detail table. |
| 3 | `ERROR_DT_TM` | DATETIME | NOT NULL |  | This column is used to store the date and time of when the user unsuccessfully attempted to re-authenticate themselves. |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 5 | `TASK_NUMBER` | DOUBLE | NOT NULL |  | This column is used to store the number of the task the user was using when unsuccessfully attempting to re-authenticate themselves. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AUTH_ERROR_DETAIL](AUTH_ERROR_DETAIL.md) | `AUTH_ERROR_ID` |

