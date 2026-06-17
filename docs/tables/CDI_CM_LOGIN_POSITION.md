# CDI_CM_LOGIN_POSITION

> This table associates users defined in the CDI_CM_LOGIN table to MIllenium user's positions.

**Description:** CDI Content Management Login Position  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_CM_LOGIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the CDI_CM_Login table. It associates a row in this table to the CDI_CM_Login table. |
| 2 | `CDI_CM_LOGIN_POSITION_ID` | DOUBLE | NOT NULL |  | This is the unique primary key of this table. |
| 3 | `POSITION_CD` | DOUBLE | NOT NULL |  | The Millennium user's position code that this user is associated with. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_CM_LOGIN_ID` | [CDI_CM_LOGIN](CDI_CM_LOGIN.md) | `CDI_CM_LOGIN_ID` |

