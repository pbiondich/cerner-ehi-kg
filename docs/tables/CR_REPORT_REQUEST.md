# CR_REPORT_REQUEST

> Logs all the report requests for the new XML/XSL Clinical Reporting solution. This table is equivalent to the original CHART_REQUEST table that is used for the original solution based on MS Word architecture.

**Description:** Report Request Table  
**Table type:** ACTIVITY  
**Primary key:** `REPORT_REQUEST_ID`  
**Columns:** 86  
**Referenced by:** 12 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_NBR` | VARCHAR(20) |  |  | This is the accession number for the results that will print on the accession level chart |
| 2 | `BEGIN_DT_TM` | DATETIME |  |  | This is the date and time that is used to determine how far back the system should look when searching for data to include on the chart. |
| 3 | `CHART_TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | Primary for a given key from the CHART_TRIGGER table. |
| 4 | `CONCEPT_SERVICE_NAME` | VARCHAR(100) |  |  | The name of the external service requesting the report. Example: Anatomic Pathology, Radiology, Cardio |
| 5 | `CONTACT_INFO` | VARCHAR(255) |  |  | The contact information defined to be included in a fax cover page and RRD report title. |
| 6 | `COPIES_NBR` | DOUBLE |  |  | Stores the number of copies to print for this chart.. |
| 7 | `CUSTODIAL_ORG_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier for the organization that owns or issues the continuity of care document (CCD) that was generated. (FK from ORGANIZATION table) |
| 8 | `DEBUG_ZIP_ID` | DOUBLE | NOT NULL | FK→ | Stores the reference back to Long_Blob table where the debug ZIP file for this report request is stored. |
| 9 | `DESTINATION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Stores the type of destination. Possible values are person, organization, or free-text. |
| 10 | `DESTINATION_VALUE_TXT` | VARCHAR(255) |  |  | The logical destination of the chart. |
| 11 | `DEX_PAYLOAD_SIZE` | DOUBLE |  |  | The size of the payload sent from Data Extraction for report generation. |
| 12 | `DIRECT_PARENT_REQUEST_ID` | DOUBLE | NOT NULL |  | DIRECT_PARENT_REQUEST_ID always points back to the request ID which was just resubmitted |
| 13 | `DISK_IDENTIFIER` | DOUBLE | NOT NULL |  | Unique number that identifies a set of requests burned to a disk |
| 14 | `DISK_LABEL` | VARCHAR(128) |  |  | label of CD/DVD that report will be burned on |
| 15 | `DISK_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of disk (DVD or CD) |
| 16 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | FK→ | This is a number which uniquely identifies a chart distribution |
| 17 | `DIST_RUN_DT_TM` | DATETIME |  |  | This is the date and time that the distribution was started |
| 18 | `DIST_RUN_TYPE_CD` | DOUBLE | NOT NULL |  | This is the code from the code set 22550 which determines what type of chart will be produced (i.e. interim, cummulative) |
| 19 | `DMS_ADHOC_FAX_NUMBER_TXT` | VARCHAR(40) |  |  | The fax number that the DMS service distributes this chart to. It is for Ad Hoc fax only. |
| 20 | `DMS_FAX_DISTRIBUTE_DT_TM` | DATETIME |  |  | The date and time that the DMS service distributes this chart. It is for fax only. |
| 21 | `DMS_SERVICE_IDENT` | VARCHAR(110) |  |  | Indicates the DMS service to send this chart to. Rplaces the DMS_SERVICE_NAME field (which was only for print devices). This new field effective on Feature 136623 - 9/07. |
| 22 | `DMS_SERVICE_NAME` | VARCHAR(64) |  |  | Obsolete ** Identifies the DMS service to send this chart to. This has been replaced by the DMS_SERVICE_IDENT field (initial release on Feature 136623 9/4/07. |
| 23 | `EMAIL_BODY_ID` | DOUBLE | NOT NULL | FK→ | The reference to the long_text row that defines the message for the email. |
| 24 | `EMAIL_SUBJECT_ID` | DOUBLE | NOT NULL | FK→ | The reference to the long_text row that defines the subject for the email. |
| 25 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 26 | `END_DT_TM` | DATETIME |  |  | This is the date and time that marks the end of the date range of data to include on the chart. |
| 27 | `EXTERNAL_CONTENT_IDENT` | VARCHAR(64) |  |  | IDENTIFIER of the external media content to be included in the report |
| 28 | `EXTERNAL_CONTENT_NAME` | VARCHAR(100) |  |  | Name of the facesheet to be included in the report |
| 29 | `FILE_MASK` | VARCHAR(255) |  |  | Mask for File Name |
| 30 | `FILE_NAME` | VARCHAR(255) |  |  | Name of the file to be saved |
| 31 | `MESSAGE_IDENT` | VARCHAR(255) |  |  | A globally unique identifier, defined when a report request is sent as an email. |
| 32 | `NON_CE_BEGIN_DT_TM` | DATETIME |  |  | This is the date/time used to determine how far back the system should look when searching for clinical insignificant data to include on the chart. |
| 33 | `NON_CE_END_DT_TM` | DATETIME |  |  | This is the date/time that marks the end of the date range for clinical insignificant data to be included on the chart. |
| 34 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the orders table. It is an internal system assigned number. |
| 35 | `OUTPUT_CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | The output content type of this chart (such as PDF, Plain Text, ort HITSP C32, etc.) Replaces the OUTPUT_CONTENT_TYPE_STR field. |
| 36 | `OUTPUT_CONTENT_TYPE_STR` | VARCHAR(255) |  |  | ** OBSOLETE ** (this column/function will be replaced by OUTPUT_CONTENT_TYPE_CD - 2010) The output content type strings should match common content type definitions according to the MIME specification (text/plain, application/pdf, etc.). |
| 37 | `OUTPUT_DEST_CD` | DOUBLE | NOT NULL | FK→ | Identifies the output destination to send this chart to. This is used for legacy output destinations. |
| 38 | `PARENT_REQUEST_ID` | DOUBLE | NOT NULL |  | When a report is resubmitted a new row will be added to the table. This attribute points back to the original report request. |
| 39 | `PATIENT_CONSENT_RECEIVED_IND` | DOUBLE | NOT NULL |  | Indicates if patient consent was received before requesting this chart. |
| 40 | `PATIENT_REQUEST_IND` | DOUBLE | NOT NULL |  | Indicates if the rfequest was made for a Patient |
| 41 | `PERSONA_TXT` | VARCHAR(100) |  |  | The type of user making the request. Example: Patient, Provider, etc. |
| 42 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 43 | `PROCESSING_TIME` | DOUBLE |  |  | Number of seconds it took to process this request |
| 44 | `PROVIDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The prsnl_id for whom the report is intended. |
| 45 | `PROVIDER_RELTN_CD` | DOUBLE | NOT NULL |  | The encounter or person level relationship the provider has with the person's chart. |
| 46 | `PRSNL_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the personnel relation associated to the request |
| 47 | `PRSNL_ROLE_PROFILE_UID` | VARCHAR(150) |  |  | The current RoleProfile UID of the user in context when the request was submitted (only used with SMR) |
| 48 | `READER_GROUP` | VARCHAR(15) |  |  | This field when defined is used to link one distribution with another |
| 49 | `RELEASE_COMMENT` | VARCHAR(1000) |  |  | Additional comments about the requesting of this chart. |
| 50 | `RELEASE_REASON_CD` | DOUBLE | NOT NULL |  | Reason for requesting the chart. Located on code set 14211. |
| 51 | `REPORT_FILE_SIZE` | DOUBLE |  |  | The file size of clinical report generated for the report request. |
| 52 | `REPORT_REQUEST_ID` | DOUBLE | NOT NULL | PK | The primary identifier that uniquely identifies a row on the table. |
| 53 | `REPORT_STATUS_CD` | DOUBLE | NOT NULL |  | Stores the status of the report request. A different code set will be used from the original chart_status_cd code set because of different statuses and potential error codes. |
| 54 | `REQUESTING_ROLE_PROFILE` | VARCHAR(255) |  |  | Stores the role profile identifier of the requesting user so that the server can establish the proper security context. |
| 55 | `REQUESTOR_TYPE_FLAG` | DOUBLE | NOT NULL |  | Stores the type of requestor. Possible values are person, organization, or free-text. |
| 56 | `REQUESTOR_VALUE_TXT` | VARCHAR(255) |  |  | The logical requestor of the chart. |
| 57 | `REQUEST_APP_NBR` | DOUBLE |  |  | Stores the requesting application number of a request. |
| 58 | `REQUEST_DT_TM` | DATETIME | NOT NULL |  | The date and time the report request was created. |
| 59 | `REQUEST_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is the prsnl_id of the person who submitted the report request. If the report was submitted by a distribution run, this field will be populated by the SYSTEM row. |
| 60 | `REQUEST_TYPE_FLAG` | DOUBLE | NOT NULL |  | This identifies the type of report request that has been submitted (i.e. ad hoc, distribution, expedite, manual expedite, document service, concept service) |
| 61 | `REQUEST_XML_ID` | DOUBLE | NOT NULL | FK→ | The LONG_TEXT row that represents the original HTTP request sent to generate this report. |
| 62 | `RESUBMIT_CNT` | DOUBLE | NOT NULL |  | This is the count of times for the report request row being resubmitted |
| 63 | `RESULT_STATUS_FLAG` | DOUBLE | NOT NULL |  | Flag to represent what type of results should be included on the chart based on their status. 1 = all statuses, 2 = verified and pending, 3 = verified only. |
| 64 | `ROUTE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to point to the unique ID for the chart route. |
| 65 | `ROUTE_STOP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to point to the unique ID for the chart_sequence_group. |
| 66 | `RRD_HANDLE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier on the OUTPUTCTX table for a report faxed by RRD. |
| 67 | `SCOPE_FLAG` | DOUBLE | NOT NULL |  | This is the scope of the report request (i.e. accession, order, encounter) |
| 68 | `SENDER_EMAIL` | VARCHAR(100) |  |  | The email address that the email request will be sent from. |
| 69 | `SEQUENCE_NBR` | DOUBLE |  |  | The relative collation sequence within a batch of requests. |
| 70 | `SERVER_FULL_NAME` | VARCHAR(250) |  |  | The description of the server that processed the request |
| 71 | `STATUS_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The reference to the long_text row that defines the status of the report request. |
| 72 | `SUMMARY_REPORT_XML_ID` | DOUBLE | NOT NULL | FK→ | The LONG_TEXT row that stores the summary XML document of what was printed in the report. This file is used for the Disclosure Audit Log. |
| 73 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | This is the number that uniquely identifies the report template used to format the report. |
| 74 | `TEMPLATE_VERSION_DT_TM` | DATETIME |  |  | The date / time of the template version used for this request. |
| 75 | `TEMPLATE_VERSION_MODE_FLAG` | DOUBLE |  |  | Indicates what version of the template should be used in the request. |
| 76 | `TOTAL_PAGES_NBR` | DOUBLE |  |  | Total pages of the report generated. |
| 77 | `TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | Trigger_id for ESO from the CQM_FSIESO_TR_1 table. |
| 78 | `TRIGGER_NAME` | VARCHAR(100) |  |  | Stores the trigger name that fired the report request. Triggers are created in the Expedite Tool and are not related to the ESO trigger_id and trigger_type. |
| 79 | `TRIGGER_TYPE` | VARCHAR(15) |  |  | Activity type of the event being charted |
| 80 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 81 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 82 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 83 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 84 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 85 | `USE_POSTING_DATE_IND` | DOUBLE | NOT NULL |  | Indicates whether or not to use the clinically relevant date or the posting date in the date range selection. |
| 86 | `XR_BITMAP` | DOUBLE |  |  | This column will be a bitmap that that can use to set various details about the request that will be useful for troubleshooting. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_TRIGGER_ID` | [CHART_TRIGGER](CHART_TRIGGER.md) | `CHART_TRIGGER_ID` |
| `CUSTODIAL_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `DEBUG_ZIP_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `DISTRIBUTION_ID` | [CHART_DISTRIBUTION](CHART_DISTRIBUTION.md) | `DISTRIBUTION_ID` |
| `EMAIL_BODY_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `EMAIL_SUBJECT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `OUTPUT_DEST_CD` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROVIDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRSNL_RELTN_ID` | [PRSNL_RELTN](PRSNL_RELTN.md) | `PRSNL_RELTN_ID` |
| `REQUEST_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REQUEST_XML_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ROUTE_ID` | [CHART_ROUTE](CHART_ROUTE.md) | `CHART_ROUTE_ID` |
| `ROUTE_STOP_ID` | [CHART_SEQUENCE_GROUP](CHART_SEQUENCE_GROUP.md) | `SEQUENCE_GROUP_ID` |
| `RRD_HANDLE_ID` | [OUTPUTCTX](OUTPUTCTX.md) | `HANDLE_ID` |
| `STATUS_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SUMMARY_REPORT_XML_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `TEMPLATE_ID` | [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_TEMPLATE_ID` |
| `TRIGGER_ID` | [CQM_FSIESO_TR_1](CQM_FSIESO_TR_1.md) | `TRIGGER_ID` |

## Referenced by (12)

| From table | Column |
|------------|--------|
| [CR_OUTPUT_DESTINATION](CR_OUTPUT_DESTINATION.md) | `REPORT_REQUEST_ID` |
| [CR_PRINTED_SECTIONS](CR_PRINTED_SECTIONS.md) | `REPORT_REQUEST_ID` |
| [CR_REPORT_REQUEST_ACTIVITY](CR_REPORT_REQUEST_ACTIVITY.md) | `REPORT_REQUEST_ID` |
| [CR_REPORT_REQUEST_ENCNTR](CR_REPORT_REQUEST_ENCNTR.md) | `REPORT_REQUEST_ID` |
| [CR_REPORT_REQUEST_EVENT](CR_REPORT_REQUEST_EVENT.md) | `REPORT_REQUEST_ID` |
| [CR_REPORT_REQUEST_SECTION](CR_REPORT_REQUEST_SECTION.md) | `REPORT_REQUEST_ID` |
| [ENCNTR_CARE_MGMT_COMM](ENCNTR_CARE_MGMT_COMM.md) | `REPORT_REQUEST_ID` |
| [RCM_POST_ACUTE_UPLOAD](RCM_POST_ACUTE_UPLOAD.md) | `REPORT_REQUEST_ID` |
| [RCM_TLC_PLACEMENT_FAC_R](RCM_TLC_PLACEMENT_FAC_R.md) | `REPORT_REQUEST_ID` |
| [RCM_TLC_SERVICE_FAC_R](RCM_TLC_SERVICE_FAC_R.md) | `REPORT_REQUEST_ID` |
| [RCM_TLC_UPLOAD](RCM_TLC_UPLOAD.md) | `REPORT_REQUEST_ID` |
| [ROI_REQUEST](ROI_REQUEST.md) | `REPORT_REQUEST_ID` |

