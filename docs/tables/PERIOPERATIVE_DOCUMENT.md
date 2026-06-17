# PERIOPERATIVE_DOCUMENT

> Contains the attributes of a perioperative document, including document type, status of document, etc.

**Description:** Perioperative Document  
**Table type:** ACTIVITY  
**Primary key:** `PERIOP_DOC_ID`  
**Columns:** 34  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 4 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 5 | `DOC_TERM_BY_ID` | DOUBLE | NOT NULL | FK→ | The person responsible for terminating this document |
| 6 | `DOC_TERM_DT_TM` | DATETIME |  |  | The date and time this document was terminated |
| 7 | `DOC_TERM_REASON_CD` | DOUBLE | NOT NULL |  | The reason this document was terminated |
| 8 | `DOC_TERM_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 9 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The document type associated with this perioperative document, i.e. OR Nursing Record, Preop Nursing Assessment, etc. |
| 10 | `LAST_PRINT_DT_TM` | DATETIME |  |  | Indicates the date and time of the last printing of the case document |
| 11 | `LAST_PRINT_TZ` | DOUBLE |  |  | Time zone for the last_print_dt_tm column. |
| 12 | `LAST_VER_DT_TM` | DATETIME |  |  | The date and time this document was last verified |
| 13 | `LAST_VER_ID` | DOUBLE | NOT NULL | FK→ | The person responsible for verifying this document last |
| 14 | `LAST_VER_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 15 | `LOCKED_APPLCTX` | DOUBLE |  |  | Locked ApplicationContextColumn |
| 16 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | *** OBSOLETE ***Column |
| 17 | `ORIG_PRINT_DT_TM` | DATETIME |  |  | Indicates the date and time of the original printing of the case document |
| 18 | `ORIG_PRINT_TZ` | DOUBLE |  |  | Time zone of the orig_print_dt_tm column. |
| 19 | `PERIOP_DOC_ID` | DOUBLE | NOT NULL | PK | The primary key, uniquely identifying a perioperative document |
| 20 | `PERIOP_DOC_TYPE_FLAG` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 21 | `REC_VER_DT_TM` | DATETIME |  |  | The date and time this document was verified |
| 22 | `REC_VER_ID` | DOUBLE | NOT NULL | FK→ | The person responsible for verifying this document |
| 23 | `REC_VER_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 24 | `RETROSPECTIVE_DOC_IND` | DOUBLE |  |  | An indicator of whether or not this document was documented retrospectively (outside of the OR). |
| 25 | `ROOM_COST_PT_DUR` | DOUBLE |  |  | The room cost associated with this perioperative document (calculated using patient in room duration) |
| 26 | `ROOM_COST_SURG_DUR` | DOUBLE |  |  | The room cost associated with this perioperative document (calculated using surgery duration) |
| 27 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | The surgical area associated with this perioperative document |
| 28 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | The surgical case associated with this perioperative document |
| 29 | `TOT_ATTENDEE_COST` | DOUBLE |  |  | The total cost of all attendees associated with this perioperative document |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOC_TERM_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LAST_VER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REC_VER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [SEGMENT_HEADER](SEGMENT_HEADER.md) | `PERIOP_DOC_ID` |
| [SN_CE_EXTRACT_ST](SN_CE_EXTRACT_ST.md) | `PERIOP_DOC_ID` |
| [SN_IMPLANT_LOG_ST](SN_IMPLANT_LOG_ST.md) | `PERIOP_DOC_ID` |
| [SN_SIGNATURE](SN_SIGNATURE.md) | `PERIOP_DOC_ID` |
| [SN_UNFINALIZE_REASON](SN_UNFINALIZE_REASON.md) | `PERIOP_DOC_ID` |

