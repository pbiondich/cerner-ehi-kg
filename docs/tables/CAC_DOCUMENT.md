# CAC_DOCUMENT

> Stores information on documents that have been parsed for computer assisted coding

**Description:** Computer Assisted Coding Documents  
**Table type:** ACTIVITY  
**Primary key:** `CAC_DOCUMENT_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BLOB_HANDLE` | VARCHAR(255) |  |  | Handle to remote blob. |
| 4 | `CAC_DOCUMENT_ID` | DOUBLE | NOT NULL | PK | Unique identifier number for this row |
| 5 | `CLINICAL_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Clinical Event ID this document belongs to |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter ID this document belongs to |
| 7 | `ENCNTR_SLICE_ID` | DOUBLE | NOT NULL | FK→ | Encounter Slice ID this document belongs to |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `EVENT_ID` | DOUBLE | NOT NULL |  | Event ID for the original version of the document |
| 10 | `FURTHER_REVIEW_REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether this document requires further review or not. 1 indicates that this document requires further review and 0 indicates that this document doesn't require further review |
| 11 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the row on the long_text table where the plain-text version of the document is stored |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person ID this document belongs to |
| 13 | `PROCESS_STATUS_CD` | DOUBLE | NOT NULL |  | A code indicating the CAC document process status. |
| 14 | `REVIEWED_IND` | DOUBLE | NOT NULL |  | Indicates that this document has been reviewed |
| 15 | `SVC_CAT_HIST_ID` | DOUBLE | NOT NULL | FK→ | Service Category History ID this document belongs to |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLINICAL_EVENT_ID` | [CLINICAL_EVENT](CLINICAL_EVENT.md) | `CLINICAL_EVENT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ENCNTR_SLICE_ID` | [ENCNTR_SLICE](ENCNTR_SLICE.md) | `ENCNTR_SLICE_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SVC_CAT_HIST_ID` | [SERVICE_CATEGORY_HIST](SERVICE_CATEGORY_HIST.md) | `SVC_CAT_HIST_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CAC_NOMENCLATURE](CAC_NOMENCLATURE.md) | `CAC_DOCUMENT_ID` |

