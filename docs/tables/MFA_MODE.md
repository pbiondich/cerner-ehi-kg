# MFA_MODE

> Mode name and description information. Stores defined MFA Modes.

**Description:** Multi Factor Authenticatin - Mode  
**Table type:** REFERENCE  
**Primary key:** `MFA_MODE_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MFA_MODE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 2 | `MODE_DESCRIPTION` | VARCHAR(200) |  |  | Free-text Description of the Mode |
| 3 | `MODE_NAME` | VARCHAR(45) | NOT NULL |  | Unique Free-text name for the Mode |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MFA_METHOD_CHAIN](MFA_METHOD_CHAIN.md) | `MFA_MODE_ID` |

