# ORDER_ALERTS

> Pharmacy order alerts

**Description:** ORDER ALERTS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Primary key to LONG_TEXT table. |
| 2 | `ACTIVE_DT_TM` | DATETIME |  |  | Active date and time |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_TYPE_CD` | DOUBLE | NOT NULL |  | Active type code |
| 5 | `ALERT_CD` | DOUBLE | NOT NULL | FK→ | primary key |
| 6 | `ALERT_TYPE_CD` | DOUBLE | NOT NULL |  | Type of order alert |
| 7 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time from which the row is valid as active current data. This may be valued with the date that the row was created. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `INACTIVE_DT_TM` | DATETIME |  |  | Date/Time the record was inactivated. |
| 10 | `PROMPT_FOR_ACTION_IND` | DOUBLE |  |  | Flag to determine is user is to be prompted for action to resolve the alert. |
| 11 | `PROMPT_FOR_REASON_IND` | DOUBLE |  |  | Flag to indicate if the user should be prompted for a reason for the alert. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VIEW_ONLY_IND` | DOUBLE |  |  | Alert is view only, no action required. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ALERT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

