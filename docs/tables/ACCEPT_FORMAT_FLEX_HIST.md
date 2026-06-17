# ACCEPT_FORMAT_FLEX_HIST

> History- Flexing options for order entry formats.

**Description:** Accept Format Flexing - hist  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_FLAG` | DOUBLE |  |  | accept flag 0 = required 1 = optional 2 = no display 3 = display only |
| 2 | `ACCEPT_FORMAT_FLEX_HIST_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 3 | `ACTION_DT_TM` | DATETIME |  |  | date and time when the Action (delete/update) was taken |
| 4 | `ACTION_TAKEN_TFLG` | VARCHAR(30) |  |  | The action taken by the user (delete/update) |
| 5 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The order action that this flexing is built for. |
| 6 | `ACTION_USER_ID` | DOUBLE |  |  | user id of the person who took the action (delete/update) |
| 7 | `CARRY_FWD_PLAN_IND` | DOUBLE | NOT NULL |  | Indicates whether to bring forward the value of this field from one order to the next for PowerPlans. The ""field"" is the front end format field which in relation to this table is the entire row of this table. A good example would be a Dose field. 1 - Carry Forward - 0- Do not Carry Forward |
| 8 | `DEFAULT_PARENT_ENTITY_ID` | DOUBLE |  |  | The identifier for the coded default values. This field will be empty (zero) for non-coded defaults. |
| 9 | `DEFAULT_PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The table that the coded default value is from. This field will be empty for non-coded defaults. |
| 10 | `DEFAULT_VALUE` | VARCHAR(100) |  |  | The default value to be used for this field flexing. |
| 11 | `FLEX_CD` | DOUBLE | NOT NULL |  | Accept format flexing code. Identifies the flex value this record is for. Depending on the flex_type_flag - this could contain a location_cd - position_cd or an application_cd. |
| 12 | `FLEX_PARENT_ENTITY_ID` | DOUBLE |  |  | Identifies the flex value this record is for. Depending on the flex_type_flag - this could contain a location_cd - position_cd or an application_cd. |
| 13 | `FLEX_PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The table that contains the flex parameter as a key. Will currently always be CODE_VALUE. |
| 14 | `FLEX_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies which type of flexing this record is for (e.g. application - position - etc.). 0 - Ordering Location - 1 - Patient Location - 2 - Application - 3 - Position - 4 - Encounter Type. |
| 15 | `LOCK_ON_MODIFY_FLAG` | DOUBLE | NOT NULL |  | Indicates if a detail is to be locked for a modify action. A 0 indicates that the detail is not locked and the accept_flag will be honored. 0 - Not locked - 1 - Locked. |
| 16 | `OE_FIELD_ID` | DOUBLE | NOT NULL |  | The order entry field that is to be flexed. |
| 17 | `OE_FORMAT_ID` | DOUBLE | NOT NULL |  | The Order entry format that is to be flexed. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

