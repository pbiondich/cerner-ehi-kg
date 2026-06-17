# SN_PREF_CARD

> Surgical Preference Card to define attributes (items, comments, etc.) for a surgical procedure

**Description:** SugiNet Preference Card  
**Table type:** REFERENCE  
**Primary key:** `SN_PREF_CARD_ID`  
**Columns:** 17  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 3 | `ARCHIVED_DT_TM` | DATETIME |  |  | The date and time the preference card was archived; |
| 4 | `ARCHIVED_IND` | DOUBLE | NOT NULL |  | Indicates whether the card is valid or has temporarily been archived; |
| 5 | `ARCHIVED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who marked the Preference Card as being archived; |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the preference card was created; |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who created the Preference Card; |
| 8 | `PREF_CARD_DESCRIPTION` | VARCHAR(500) |  |  | Description of the Preference Card; |
| 9 | `PREF_CARD_NAME` | VARCHAR(150) | NOT NULL |  | Name of the Preference Card; |
| 10 | `PREF_CARD_NAME_KEY` | VARCHAR(150) | NOT NULL |  | Indexed name of preference Card; |
| 11 | `SN_PREF_CARD_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 12 | `SURG_AREA_CD` | DOUBLE | NOT NULL | FK→ | Surgical Area Code; |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ARCHIVED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SURG_AREA_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [SCHED_CASE_PICK_LIST](SCHED_CASE_PICK_LIST.md) | `SN_PREF_CARD_ID` |
| [SN_PICKLIST_PREF_CARD_R](SN_PICKLIST_PREF_CARD_R.md) | `SN_PREF_CARD_ID` |
| [SN_PICKLIST_REQUEST_PC](SN_PICKLIST_REQUEST_PC.md) | `SN_PREF_CARD_ID` |
| [SN_PREF_CARD_COMMENT](SN_PREF_CARD_COMMENT.md) | `SN_PREF_CARD_ID` |
| [SN_PREF_CARD_EXCEPTION](SN_PREF_CARD_EXCEPTION.md) | `SN_PREF_CARD_ID` |
| [SN_PREF_CARD_ITEM](SN_PREF_CARD_ITEM.md) | `SN_PREF_CARD_ID` |
| [SN_PREF_CARD_LOCK](SN_PREF_CARD_LOCK.md) | `SN_PREF_CARD_ID` |
| [SN_PREF_CARD_MODIFY_HIST](SN_PREF_CARD_MODIFY_HIST.md) | `SN_PREF_CARD_ID` |
| [SN_PREF_CARD_PROCEDURE](SN_PREF_CARD_PROCEDURE.md) | `SN_PREF_CARD_ID` |

