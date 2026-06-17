# PL_DEFAULTS

> This table stores global default settings for

**Description:** This table stores global default settings  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVATE_PERSON_IND` | DOUBLE |  |  | Indicates whether person level security is turned on or not. |
| 2 | `ADDRESS_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 3 | `ADD_PHYS_IND` | DOUBLE |  |  | Indicates whether or not the user will be allowed to add free text physicians. |
| 4 | `AGE_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 5 | `BIRTH_DATE_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 6 | `BIRTH_TIME_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 7 | `BUSINESS_PHONE_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 8 | `CITY_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 9 | `FIRST_NAME_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 10 | `HOME_PHONE_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 11 | `LANGUAGE_FLAG` | DOUBLE |  |  | This field contains a flag indicating whether language is a required field during registration for client and patient bill types. 0 - Neither, 1 - Client, 2 - Patient, 3 - Both, 4 - Disable |
| 12 | `MIDDLE_NAME_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 13 | `ORDER_COMMENT_FLAG` | DOUBLE |  |  | Indicates comments and/or notes can be added or modfied. |
| 14 | `PL_DEFAULTS_KEY` | VARCHAR(10) | NOT NULL |  | Table Key |
| 15 | `RACE_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 16 | `ROOT_MENU_NODE` | VARCHAR(20) |  |  | Custom description for the root menu node for Webtop |
| 17 | `SEX_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 18 | `SSN_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 19 | `STATE_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `ZIP_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

