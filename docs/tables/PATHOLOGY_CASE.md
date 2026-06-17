# PATHOLOGY_CASE

> This activity table contains a single record for every pathology case included in the PathNet Anatomic Pathology system. It is a key table for most queries (every case has a record included), and the records are maintained indefinately.

**Description:** Pathology Case  
**Table type:** ACTIVITY  
**Primary key:** `CASE_ID`  
**Columns:** 43  
**Referenced by:** 13 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSIONED_DT_TM` | DATETIME |  |  | This field includes the date and time the case was accessioned. |
| 2 | `ACCESSION_NBR` | CHAR(21) |  |  | This field includes the case number assigned to the pathology case. |
| 3 | `ACCESSION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the user who accessioned the case (the user who caused the row to be added to the PATHOLOGY_CASE table. This value could be used to join to information on the PRSNL and PERSON tables. |
| 4 | `AUTOPSY_DESCRIPTION` | VARCHAR(100) |  |  | This field is not used at this time. |
| 5 | `AUTOPSY_SCOPE_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 6 | `BLOB_BITMAP` | DOUBLE |  |  | This column indicates whether or not there is any additional blob data associated with this case row (i.e. case images). |
| 7 | `CANCEL_CD` | DOUBLE | NOT NULL |  | If the case is cancelled, this field contains the identification code associated with the cancellation reason. |
| 8 | `CANCEL_DT_TM` | DATETIME |  |  | If the case is cancelled, this field contains the date and time the cancellation event occurred. |
| 9 | `CANCEL_ID` | DOUBLE | NOT NULL | FK→ | If the case is cancelled, this field contains the internal identification code of the user who executed the cancellation event. This value could be used to join to user information stored on the PRSNL and PERSON tables. |
| 10 | `CASE_COLLECT_DT_TM` | DATETIME |  |  | This field includes the collection date and time associated with the case. Note that collection date and time information specific to the specimen(s) submitted for the case is stored on the CASE_SPECIMEN table. |
| 11 | `CASE_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies a row included on the PATHOLOGY_CASE table. This field is used to represent a pathology case, and would be used to join to other tables (as a foreign key) such as the CASE_REPORT and CASE_SPECIMEN tables. CASE_ID is derived from ACCESSION.ACCESSION_ID. |
| 12 | `CASE_NUMBER` | DOUBLE | NOT NULL |  | This field includes the sequential number portion of the case (accession) number. The entire number is stored in the ACCESSION_NBR field. |
| 13 | `CASE_RECEIVED_DT_TM` | DATETIME |  |  | This field includes the received date and time associated with the case. Note that the received date and time information specific to the specimen(s) submitted for the case is stored on the CASE_SPECIMEN table. |
| 14 | `CASE_TYPE_CD` | DOUBLE | NOT NULL |  | This field includes the identification code associated with the case type value. The case type is used to generically categorize the case based on the accession prefix value. Examples of case types include surgical, gyn, non-gyn, and autopsy. |
| 15 | `CASE_YEAR` | DOUBLE | NOT NULL |  | This field includes the year portion of the case (accession) number. The entire number is stored in the ACCESSION_NBR field. |
| 16 | `CHR_IND` | DOUBLE |  |  | This indicator value specifies, for a pathology case, whether or not the patient was flagged as being at "clinical high risk (CHR)" for developing cervical cancer. If a value exists in the MAIN_REPORT_COMPLETE_DT_TM field for the case, the CHR flag is classified as a final (historical) flag. If a date/time value does not exist, the flag is classified as a preliminary flag. |
| 17 | `COMMENTS` | VARCHAR(255) |  |  | This field is no longer used. Refer to the COMMENTS_LONG_TEXT_ID for information regarding the pathology case comment. |
| 18 | `COMMENTS_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the LONG_TEXT table that contains the pathology case comment. |
| 19 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 20 | `DATASET_UID` | VARCHAR(128) |  |  | This field contains the dataset UID string that will be assigned for this case. Each DICOM image that is attached to this case will use this dataset UID string. |
| 21 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 22 | `EXT_ACCESSION_NBR` | CHAR(21) |  |  | This field contains the 'accession_nbr' from a contributor_system_cd. This field is only field out on a AP history upload. |
| 23 | `GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to accession group information. Accession group information is stored in common tables, and AP-specific accession group information is stored on the PREFIX_GROUP table. |
| 24 | `INTERFACE_SEND_CNT` | DOUBLE | NOT NULL |  | This field counts the number of times a case is interfaced to a foreign system is sent outbound. |
| 25 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the "building" portion of the ordering location value, if specified. This value could be used to join to location-specific information stored on the LOCATION table and associated codesets. |
| 26 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the "facility" portion of the ordering location value, if specified. This value could be used to join to location-specific information stored on the LOCATION table and associated codesets. |
| 27 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the "nursing station" portion of the ordering location value, if specified. This value could be used to join to location-specific information stored on the LOCATION table and associated codesets. |
| 28 | `MAIN_REPORT_CMPLETE_DT_TM` | DATETIME |  |  | This field contains the date and time the primary report associated with the case was verified. |
| 29 | `NEXT_FOREIGN_WS_NBR` | DOUBLE | NOT NULL |  | Maintains the next available foreign worksheet number for a pathology case. |
| 30 | `ORIGIN_FLAG` | DOUBLE |  |  | This field contains a flag value documenting how the case was added to the PATHOLOGY_CASE table. Cases can be added by accessioning, cases can be added to history manually, and cases can be added to history via an interface, for example. |
| 31 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 32 | `PREFIX_ID` | DOUBLE | NOT NULL |  | This field includes the identification code representing the prefix portion of the case (accession) number. The entire number is stored in the ACCESSION_NBR field. Accession prefix information is stored on the AP_PREFIX table. |
| 33 | `RECEIVED_SMEAR_IND` | DOUBLE |  |  | Indicator value specifies whether the gynecological smears for the case were received from outside the laboratory. |
| 34 | `REQUESTING_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | This field includes the internal identification code associated with the physician who is designated as the requesting physician for this case. Other physicians for this case (copy to physicians) are stored on the CASE_PROVIDER table. |
| 35 | `RESERVED_IND` | DOUBLE |  |  | This field includes an indicator documenting whether or not the case is accession number is in a reserved status. |
| 36 | `RESPONSIBLE_PATHOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | This field includes the internal identification code associated with the pathologist assigned to the case, if present. This value could be used to join to user information stored on the PRSNL and PERSON tables. |
| 37 | `RESPONSIBLE_RESIDENT_ID` | DOUBLE | NOT NULL | FK→ | This field includes the internal identification code associated with the resident assigned to the case, if present. This value could be used to join to user information stored on the PRSNL and PERSON tables. |
| 38 | `SOURCE_OF_SMEAR_CD` | DOUBLE | NOT NULL |  | This field contains the identification code associated with the source of the gynecological smears for the case. Examples would be GP, GUM, and NHS Hospital |
| 39 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCESSION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `CANCEL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `COMMENTS_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `GROUP_ID` | [PREFIX_GROUP](PREFIX_GROUP.md) | `GROUP_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REQUESTING_PHYSICIAN_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RESPONSIBLE_PATHOLOGIST_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RESPONSIBLE_RESIDENT_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (13)

| From table | Column |
|------------|--------|
| [AP_DC_EVENT](AP_DC_EVENT.md) | `CASE_ID` |
| [AP_DC_EVENT](AP_DC_EVENT.md) | `CORRELATE_CASE_ID` |
| [AP_DIGITAL_SLIDE](AP_DIGITAL_SLIDE.md) | `CASE_ID` |
| [AP_FT_EVENT](AP_FT_EVENT.md) | `CASE_ID` |
| [AP_IMAGE_MIGRATED](AP_IMAGE_MIGRATED.md) | `CASE_ID` |
| [AP_QA_INFO](AP_QA_INFO.md) | `CASE_ID` |
| [CASE_PROVIDER](CASE_PROVIDER.md) | `CASE_ID` |
| [CASE_REPORT](CASE_REPORT.md) | `CASE_ID` |
| [CASE_SPECIMEN](CASE_SPECIMEN.md) | `CASE_ID` |
| [CYTO_SCREENING_EVENT](CYTO_SCREENING_EVENT.md) | `CASE_ID` |
| [FT_TERM_CANDIDATE_LIST](FT_TERM_CANDIDATE_LIST.md) | `REVIEW_CASE_ID` |
| [PROCESSING_TASK](PROCESSING_TASK.md) | `CASE_ID` |
| [REPORT_DETAIL_TASK](REPORT_DETAIL_TASK.md) | `CASE_ID` |

