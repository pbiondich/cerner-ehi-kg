# PREF_CARD_SEGMENT

> Contains the segments associated with a preference card. This list of segments will be used in Perioperative Document Manager when a case is scheduled with this surgeon/procedure

**Description:** Preference Card Segment  
**Table type:** REFERENCE  
**Primary key:** `PREF_CARD_SEG_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 6 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 8 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 9 | `DEFAULTS_EXIST_IND` | DOUBLE |  |  | An indicator of whether or not preference card defaults exist for this segment |
| 10 | `INPUT_FORM_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 11 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | *** OBSOLETE ***Column |
| 12 | `PREF_CARD_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the preference_card table indicating the preference card associated with this segment |
| 13 | `PREF_CARD_SEG_ID` | DOUBLE | NOT NULL | PK | The primary key, uniquely identifying a row on this table |
| 14 | `SEG_CD` | DOUBLE | NOT NULL |  | The segment associated with this preference card |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PREF_CARD_ID` | [PREFERENCE_CARD](PREFERENCE_CARD.md) | `PREF_CARD_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PREF_CARD_DEFAULT](PREF_CARD_DEFAULT.md) | `PREF_CARD_SEG_ID` |

