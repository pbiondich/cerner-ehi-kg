# PREFERENCE_CARD

> Contains the attributes of a surgeon/procedure preference card, including surgical specialty, historical average, etc.

**Description:** Preference Card  
**Table type:** REFERENCE  
**Primary key:** `PREF_CARD_ID`  
**Columns:** 33  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The surgical procedure associated with this preference card |
| 6 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table. |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 8 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 9 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 10 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 11 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The type of document that this preference card is used for. |
| 12 | `HIST_AVG_DUR` | DOUBLE |  |  | The historical average duration for this surgeon performing this procedure. |
| 13 | `LAST_USED_DT_TM` | DATETIME |  |  | The date and time the Preference Card was used for documentation. This is updated on Finalize. |
| 14 | `LOCKED_APPLCTX` | DOUBLE |  |  | Locked Application ContextColumn |
| 15 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 16 | `NUM_CASES_REC_AVG` | DOUBLE |  |  | Number of cases to use for recent average |
| 17 | `OVERRIDE_HIST_AVG_DUR` | DOUBLE |  |  | An override value for the historical average duration for this preference card. Should only be used if the actual historical average duration has become very inaccurate. Once this is changed, the historical average duration will "roll into" the override value. |
| 18 | `OVERRIDE_LOOKBACK_NBR` | DOUBLE |  |  | The number of cases to lookback in calculating the Recent Average Duration. |
| 19 | `OVERRIDE_TOT_NBR_CASES` | DOUBLE |  |  | An override value for the total number of cases for this surgeon/procedure. This will be used in calculating the historical average duration. |
| 20 | `PREF_CARD_ID` | DOUBLE | NOT NULL | PK | The primary key, uniquely identifying a preference card. |
| 21 | `PREF_CARD_TYPE_FLAG` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 22 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The provider associated with this preference card. |
| 23 | `REC_AVG_DUR` | DOUBLE |  |  | Recent Average DurationColumn |
| 24 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | The surgical area associated with this preference card |
| 25 | `SURG_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | The surgical specialty associated with this preference card, i.e. Orthopedics, ENT, etc. The value is a reference (foreign key) to the prsnl_group table with a CDF meaning of "SURGSPEC". |
| 26 | `TEMPLATE_DESC_CD` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 27 | `TEMPLATE_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 28 | `TOT_NBR_CASES` | DOUBLE |  |  | The total number of cases performed for this surgeon/procedure. Used in the calculation of historical average duration. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SURG_SPECIALTY_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [PREF_CARD_PICK_LIST](PREF_CARD_PICK_LIST.md) | `PREF_CARD_ID` |
| [PREF_CARD_SEGMENT](PREF_CARD_SEGMENT.md) | `PREF_CARD_ID` |
| [SCHED_CASE_PICK_LIST](SCHED_CASE_PICK_LIST.md) | `PREF_CARD_ID` |
| [SCH_PEND_SURG_ITEM](SCH_PEND_SURG_ITEM.md) | `PREF_CARD_ID` |
| [SN_PICKLIST_PREF_CARD_R](SN_PICKLIST_PREF_CARD_R.md) | `PREF_CARD_ID` |
| [SN_PICKLIST_REQUEST_PC](SN_PICKLIST_REQUEST_PC.md) | `PREF_CARD_ID` |
| [SN_PREFCARD_MPAGE_SNOOZE](SN_PREFCARD_MPAGE_SNOOZE.md) | `PREF_CARD_ID` |
| [SN_SURG_CASE_PROC_DOC](SN_SURG_CASE_PROC_DOC.md) | `PREF_CARD_ID` |

