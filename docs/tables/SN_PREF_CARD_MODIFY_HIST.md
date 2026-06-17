# SN_PREF_CARD_MODIFY_HIST

> Contains history of what changes are made to a preference card

**Description:** SugiNet Preference Card Modification History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MODIFY_DT_TM` | DATETIME |  |  | Date and Time a modification was made to the preference card; |
| 2 | `MODIFY_LOCK_ID` | DOUBLE |  | FK→ | The preference card lock that was used to make the modification |
| 3 | `MODIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | User who made a modification to a preference card |
| 4 | `MODIFY_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of data that was modified on the preference card - Preference Card - Procedure - Item - Exception - Comment; |
| 5 | `SN_PREF_CARD_ID` | DOUBLE |  | FK→ | Preference Card associated to the modification history; |
| 6 | `SN_PREF_CARD_MODIFY_HIST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MODIFY_LOCK_ID` | [SN_PREF_CARD_LOCK](SN_PREF_CARD_LOCK.md) | `SN_PREF_CARD_LOCK_ID` |
| `MODIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SN_PREF_CARD_ID` | [SN_PREF_CARD](SN_PREF_CARD.md) | `SN_PREF_CARD_ID` |

