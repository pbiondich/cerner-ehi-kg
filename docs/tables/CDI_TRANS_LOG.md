# CDI_TRANS_LOG

> This table holds the transaction rows of an indexed document submittal, failure, delete, and send to service for CDI applications and components.

**Description:** CDI Transaction log.  
**Table type:** ACTIVITY  
**Primary key:** `CDI_TRANS_LOG_ID`  
**Columns:** 42  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Date and time the action occurred. |
| 2 | `ACTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Description of the action. Submit = 0, Failed = 1, Send to service = 2, Delete =3, Modify = 4, Single document capture = 5, Receive = 6, Validate Manually = 7, Migrate = 8, Update Metadata = 9, Print = 10, Combine = 11, Split = 12, Copy = 13. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `AX_APPID` | DOUBLE | NOT NULL |  | The Application Identification from the OTG database for this document. |
| 5 | `AX_DOCID` | DOUBLE | NOT NULL |  | The document Identification from the OTG database for this document. |
| 6 | `BATCH_NAME` | VARCHAR(255) | NOT NULL |  | Batch name from the document index. |
| 7 | `BATCH_NAME_KEY` | VARCHAR(255) | NOT NULL |  | Batch Name converted to upper case for case-insensitive indexed queries. |
| 8 | `BLOB_HANDLE` | VARCHAR(255) |  |  | Handle to the image stored in OTG DB. |
| 9 | `BLOB_REF_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the BLOB_REFERENCE table. |
| 10 | `BLOB_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates if image is a clinical event (0 - event id is valid), non-clinical event (1 - blob ref id is valid), or neither (2 - additional info store on ext table). |
| 11 | `CDI_FORM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the cdi_form table. Only populated if an action is performed on a patient form. |
| 12 | `CDI_PENDING_DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | The ID of the pending document that the log row is related to. |
| 13 | `CDI_QUEUE_CD` | DOUBLE | NOT NULL |  | Queue the document was in prior to the transaction. |
| 14 | `CDI_TRANS_LOG_ID` | DOUBLE | NOT NULL | PK | Unique identifier generated for each row of data. |
| 15 | `COPY_CNT` | DOUBLE | NOT NULL |  | The number of copies printed. |
| 16 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time when the batch was created. |
| 17 | `DEVICE_NAME` | VARCHAR(200) |  |  | The name of the device that performed the action, such as the printer name. |
| 18 | `DOCUMENT_TYPE_ALIAS` | VARCHAR(255) |  |  | Alias for this document type's event code. |
| 19 | `DOC_TYPE` | VARCHAR(50) |  |  | Document type alias or value used to index the document. |
| 20 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 21 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event code for the document. |
| 22 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the Clinical Event Table |
| 23 | `EXTERNAL_BATCH_IDENT` | DOUBLE | NOT NULL |  | The identifier of the external batch. |
| 24 | `FINANCIAL_NBR` | VARCHAR(200) |  |  | The enctr_nbr field from the document index. A financial_nbr in Cerner. |
| 25 | `MAN_QUEUE_CAT_CD` | DOUBLE | NOT NULL |  | Manual queue category code indicating high level reason doc sent to manual queue. |
| 26 | `MAN_QUEUE_ERR_CD` | DOUBLE | NOT NULL |  | Manual queue error code indicating specific error that send doc to manual queue. |
| 27 | `MRN` | VARCHAR(200) |  |  | The MRN from the document index. |
| 28 | `PAGE_CNT` | DOUBLE | NOT NULL |  | Number of pages in the document |
| 29 | `PAGE_DELETED_CNT` | DOUBLE | NOT NULL |  | Number of pages deleted in the document before transaction. |
| 30 | `PARENT_ENTITY_ALIAS` | VARCHAR(200) | NOT NULL |  | This field contains the parent alias that was used to index the associated document. |
| 31 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This field contrains the unique primary identifier for the row from the parent table identified in field parent_entity_name. |
| 32 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | This field contains the name of the table that this cdi_trans_log row is associated to. |
| 33 | `PATIENT_NAME` | VARCHAR(255) |  |  | The patient name index information from the document index. |
| 34 | `PERF_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel Id of the person that performed the document activity. |
| 35 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 36 | `REASON_CD` | DOUBLE | NOT NULL |  | Indicates the reason for the transaction. |
| 37 | `SUBJECT` | VARCHAR(255) |  |  | Free text subject of the document used in indexing. |
| 38 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BLOB_REF_ID` | [BLOB_REFERENCE](BLOB_REFERENCE.md) | `BLOB_REF_ID` |
| `CDI_FORM_ID` | [CDI_FORM](CDI_FORM.md) | `CDI_FORM_ID` |
| `CDI_PENDING_DOCUMENT_ID` | [CDI_PENDING_DOCUMENT](CDI_PENDING_DOCUMENT.md) | `CDI_PENDING_DOCUMENT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERF_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CDI_TRANS_MOD_DETAIL](CDI_TRANS_MOD_DETAIL.md) | `CDI_TRANS_LOG_ID` |

