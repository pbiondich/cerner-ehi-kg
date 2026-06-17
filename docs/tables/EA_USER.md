# EA_USER

> Represents a USER in the system

**Description:** USER  
**Table type:** REFERENCE  
**Primary key:** `EA_USER_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_OWNER_NAME` | VARCHAR(100) |  |  | The name of the entity that possesses the user account. |
| 2 | `DIRECTORY_IND` | DOUBLE | NOT NULL |  | Indicates WHERE the user's password is maintained -1 Not a directory user0 Use Authview default (show -defaults)1 Is a directory user |
| 3 | `EA_USER_ID` | DOUBLE | NOT NULL | PK | Generated unique identifier for a user record. |
| 4 | `LOGIN_FAILURE_CNT` | DOUBLE | NOT NULL |  | The number of login failures incurred by this user since its last successful login. |
| 5 | `MIN_PASSWORD_LENGTH` | DOUBLE | NOT NULL |  | Minimum length required of the user's password (when set). |
| 6 | `PASSWORD_CHANGE_DT_TM` | DATETIME |  |  | The date/time at which the password last changed. |
| 7 | `PASSWORD_HASH` | VARCHAR(200) |  |  | Password hash value |
| 8 | `PASSWORD_LIFETIME` | DOUBLE | NOT NULL |  | The total number of days that passwords for this user are to remain valid, after which they expire. |
| 9 | `REALM` | VARCHAR(100) | NOT NULL |  | The realm or domain with which the user account is associated. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `USERNAME` | VARCHAR(100) | NOT NULL |  | Textual identifier for a user record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [EA_PASSWORD_HISTORY](EA_PASSWORD_HISTORY.md) | `EA_USER_ID` |
| [EA_USER_ATTRIBUTE_RELTN](EA_USER_ATTRIBUTE_RELTN.md) | `EA_USER_ID` |

