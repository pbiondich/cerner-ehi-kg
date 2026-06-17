# SYS_CHG_MESSAGE

> Contains reference information about the non-passive changes introduced into the system.

**Description:** system change message  
**Table type:** REFERENCE  
**Primary key:** `MESSAGE_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CATEGORY` | VARCHAR(60) |  |  | A textual description of the category of this message. |
| 5 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the message was added to the system. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | A foreign key to the LONG_TEXT_REFERENCE table representing the contents of the message. |
| 8 | `MESSAGE_ID` | DOUBLE | NOT NULL | PK | Unique identifier for this row |
| 9 | `MESSAGE_KEY` | VARCHAR(40) | NOT NULL |  | A unique key distributed by Cerner to identify this message. |
| 10 | `SUBJECT` | VARCHAR(100) |  |  | A textual description of the subject of this message |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SYS_CHG_MESSAGE_R](SYS_CHG_MESSAGE_R.md) | `MESSAGE_ID` |
| [SYS_CHG_NOTIFICATION](SYS_CHG_NOTIFICATION.md) | `MESSAGE_ID` |

