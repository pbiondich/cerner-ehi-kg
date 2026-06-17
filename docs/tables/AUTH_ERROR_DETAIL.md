# AUTH_ERROR_DETAIL

> This activity table is used to record additional logging information when a user attempts to reauthenticate themselves incorrectly three consecutive times.

**Description:** Auth_Error_Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTH_ERROR_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row on the Auth_Error_Detail table in conjunction with the sequence field. |
| 2 | `DISPLAY_LABEL` | VARCHAR(40) |  |  | This field is used as a data label for the display_value field when printing the CCL audit for the Auth_Error table. |
| 3 | `DISPLAY_VALUE` | VARCHAR(40) |  |  | This field is used as to hold additional logging information when printing the CCL audit for the Auth_Error table. |
| 4 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field uniquely identifies a row on the Auth_Error_Detail table in conjunction with the auth_error_id field. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTH_ERROR_ID` | [AUTH_ERROR](AUTH_ERROR.md) | `AUTH_ERROR_ID` |

