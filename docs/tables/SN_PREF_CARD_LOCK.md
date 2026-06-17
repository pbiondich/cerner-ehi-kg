# SN_PREF_CARD_LOCK

> Lock information when a preference card is updated

**Description:** SugiNet Preference Card Lock  
**Table type:** ACTIVITY  
**Primary key:** `SN_PREF_CARD_LOCK_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BREAK_TYPE_FLAG` | DOUBLE | NOT NULL |  | How the lock was unlocked, through normal process or broken by another user. 0 = Not broken - normal unlock. 1 = Broken by current user in a different session. 2 = Lock was expired and broken by another user. 3 = Lock was forcibly broken prior to expiring |
| 3 | `LAST_UPDT_DT_TM` | DATETIME |  |  | The last time the preference card was updated. This is used to determine if a lock is eligible to be broken; |
| 4 | `LOCK_DT_TM` | DATETIME |  |  | Date and Time the lock was acquired; |
| 5 | `LOCK_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The provider who obtained the lock; |
| 6 | `SN_PREF_CARD_ID` | DOUBLE |  | FK→ | Preference Card that the lock applies to; |
| 7 | `SN_PREF_CARD_LOCK_ID` | DOUBLE | NOT NULL | PK | PRIMAR KEY |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCK_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SN_PREF_CARD_ID` | [SN_PREF_CARD](SN_PREF_CARD.md) | `SN_PREF_CARD_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_PREF_CARD_MODIFY_HIST](SN_PREF_CARD_MODIFY_HIST.md) | `MODIFY_LOCK_ID` |

