# CASE_SPECIMEN

> This activity table contains entries for all cases having one or more specimens associated. The case/specimen relationship is stored. Specimen-specific parameters entered by the user accessioning the case are stored.

**Description:** Case Specimen  
**Table type:** ACTIVITY  
**Primary key:** `CASE_SPECIMEN_ID`  
**Columns:** 29  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADEQUACY_IND` | DOUBLE |  |  | This field is not used at this time. |
| 2 | `CANCEL_CD` | DOUBLE | NOT NULL |  | If the specimen was cancelled, this field includes the cancellation reason code associated with the cancellation activity. |
| 3 | `CASE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to case information stored on the PATHOLOGY_CASE activity table. |
| 4 | `CASE_SPECIMEN_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies a row on the CASE_SPECIMEN table (a case-specimen relationship). This field would be used to join to other tables (as a foreign key) such as the CASSETTE table. |
| 5 | `COLLECT_DT_TM` | DATETIME |  |  | This field includes the date and time the specimen was collected. |
| 6 | `DISCARD_DT_TM` | DATETIME |  |  | The date and time the specimen was disposed. |
| 7 | `DISCARD_REASON_CD` | DOUBLE | NOT NULL |  | The reason why the specimen was disposed. |
| 8 | `FIXATIVE_ADDED_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 9 | `FROZEN_REPORT_ID` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 10 | `INADEQUACY_REASON_CD` | DOUBLE | NOT NULL |  | If the specimen was documented as inadequate in the Maintain Case application, this field includes the identification code associated with the inadequacy reason. Specimen inadequacy reasons are stored on codeset 1318. |
| 11 | `LABEL_CREATE_DT_TM` | DATETIME |  |  | The date and time the last label was created. |
| 12 | `LABEL_CREATE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of method used to creat the label.0 = Spooled,1 = Flat File3 = Nice Label Flat File |
| 13 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 14 | `ON_LOAN_LOCN_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 15 | `ORIGINAL_STORAGE_DT_TM` | DATETIME |  |  | The date and time the specimen was placed in storage. |
| 16 | `RECEIVED_DT_TM` | DATETIME |  |  | This field includes the date and time the specimen was received. |
| 17 | `RECEIVED_FIXATIVE_CD` | DOUBLE | NOT NULL |  | If the specimen was associated with a fixative in the Maintain Case application, this field includes the identification code associated with the fixative. Fixatives are stored on codeset 1302. |
| 18 | `RECEIVED_ID` | DOUBLE | NOT NULL |  | This field includes the internal identification code associated with the user who updated the specimen to a received [in pathology] status. This value could be used to join to personnel information on the PRSNL and PERSON tables. |
| 19 | `SPECIAL_COMMENTS` | VARCHAR(200) |  |  | This field is no longer used. Please refer to the SPEC_COMMENT_LONG_TEXT_ID for information regarding the specimen commentl. |
| 20 | `SPECIMEN_CD` | DOUBLE | NOT NULL |  | This field stores the internal identification code associated with the specimen submitted. Specimens are stored on codeset 1306. |
| 21 | `SPECIMEN_DESCRIPTION` | VARCHAR(255) |  |  | This field stores the description associated with the specimen. |
| 22 | `SPECIMEN_TAG_ID` | DOUBLE | NOT NULL | FK→ | This field stores the reference to the actual identification code value associated with the specimen. The identification code values are stored on the AP_TAG reference table. |
| 23 | `SPEC_COMMENTS_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the LONG_TEXT table that contains the specimen comment. |
| 24 | `STORAGE_LOCN_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |
| `SPECIMEN_TAG_ID` | [AP_TAG](AP_TAG.md) | `TAG_ID` |
| `SPEC_COMMENTS_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [AP_CASE_SYNOPTIC_WS](AP_CASE_SYNOPTIC_WS.md) | `CASE_SPECIMEN_ID` |
| [CASSETTE](CASSETTE.md) | `CASE_SPECIMEN_ID` |
| [PROCESSING_TASK](PROCESSING_TASK.md) | `CASE_SPECIMEN_ID` |
| [SLIDE](SLIDE.md) | `CASE_SPECIMEN_ID` |

