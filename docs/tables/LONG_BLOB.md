# LONG_BLOB

> A core Table used to store large binary data (LONG RAW) from the corresponding table referenced in the PARENT_ENTITY_NAME column.

**Description:** Long Binary Large Object  
**Table type:** ACTIVITY  
**Primary key:** `LONG_BLOB_ID`  
**Columns:** 15  
**Referenced by:** 50 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BLOB_LENGTH` | DOUBLE | NOT NULL |  | original length of the blob. This should be the uncompressed length if the blob is compressed. |
| 6 | `COMPRESSION_CD` | DOUBLE | NOT NULL |  | compression code from code set 120. This indicates the type of compression used, if blob is compressed. |
| 7 | `LONG_BLOB` | LONGBLOB |  |  | LONG RAW defined column stores large binary data from the corresponding table referenced in the PARENT_ENTITY_NAME column. |
| 8 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for each row |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The Unique Identifier from the corresponding table name referenced in PARENT_ENTITY_NAME for which the large binary data is stored. |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The Referenced Table Name for which the large binary data is stored. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (50)

| From table | Column |
|------------|--------|
| [ACT_PW_COMP](ACT_PW_COMP.md) | `DOSE_INFO_HIST_BLOB_ID` |
| [ACT_PW_COMP](ACT_PW_COMP.md) | `LONG_BLOB_ID` |
| [BB_EDN_ADMIN](BB_EDN_ADMIN.md) | `LONG_BLOB_ID` |
| [BH_GROUP_DOC](BH_GROUP_DOC.md) | `GOALS_LONG_BLOB_ID` |
| [BH_GROUP_DOC](BH_GROUP_DOC.md) | `NOTES_LONG_BLOB_ID` |
| [BLOB_SUMMARY_REF](BLOB_SUMMARY_REF.md) | `LONG_BLOB_ID` |
| [BR_LONG_BLOB_RELTN](BR_LONG_BLOB_RELTN.md) | `LONG_BLOB_ID` |
| [CCL_LAYOUT_SECTION](CCL_LAYOUT_SECTION.md) | `SECTION_BLOB_ID` |
| [CHART_REQUEST_ARCHIVE](CHART_REQUEST_ARCHIVE.md) | `LONG_BLOB_ID` |
| [CLINICAL_NOTE_TEMPLATE](CLINICAL_NOTE_TEMPLATE.md) | `LONG_BLOB_ID` |
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `DEBUG_ZIP_ID` |
| [CR_REPORT_REQUEST_ARCHIVE](CR_REPORT_REQUEST_ARCHIVE.md) | `LONG_BLOB_ID` |
| [CT_DOCUMENT_VERSION](CT_DOCUMENT_VERSION.md) | `LONG_BLOB_ID` |
| [DA_DOCUMENT](DA_DOCUMENT.md) | `GENERATED_DATA_ID` |
| [DA_DOCUMENT](DA_DOCUMENT.md) | `GENERATED_DOC_ID` |
| [DA_DOCUMENT](DA_DOCUMENT.md) | `REPORT_PARMS_ID` |
| [DD_EMR_EXTRACT](DD_EMR_EXTRACT.md) | `EXTRACT_XML_BLOB_ID` |
| [DD_SDOC_ATTR_MENU_ITEM](DD_SDOC_ATTR_MENU_ITEM.md) | `COMMENT_BLOB_ID` |
| [DD_SDOC_ATTR_MENU_ITEM](DD_SDOC_ATTR_MENU_ITEM.md) | `RENDERED_TEXT_BLOB_ID` |
| [DIAGNOSIS](DIAGNOSIS.md) | `LONG_BLOB_ID` |
| [DMS_MEDIA_INSTANCE](DMS_MEDIA_INSTANCE.md) | `LONG_BLOB_ID` |
| [DMS_MEDIA_SIGNATURE](DMS_MEDIA_SIGNATURE.md) | `SIGNATURE_BLOB_ID` |
| [EEM_LOG_BLOB](EEM_LOG_BLOB.md) | `LONG_BLOB_ID` |
| [EKS_NOTIFICATION_BLOB_R](EKS_NOTIFICATION_BLOB_R.md) | `LONG_BLOB_ID` |
| [ENCNTR_CLIN_REVIEW](ENCNTR_CLIN_REVIEW.md) | `RESULT_XML_LONG_BLOB_ID` |
| [ENCNTR_CLIN_REVIEW_RESULT](ENCNTR_CLIN_REVIEW_RESULT.md) | `RESULT_LONG_BLOB_ID` |
| [ENCNTR_CLIN_REVIEW_RESULT](ENCNTR_CLIN_REVIEW_RESULT.md) | `RESULT_TEXT_LONG_BLOB_ID` |
| [ESI_LOG](ESI_LOG.md) | `LONG_BLOB_ID` |
| [HE_KNOWLEDGEBASE](HE_KNOWLEDGEBASE.md) | `VERSION_BLOB_ID` |
| [HE_OBJECT_ENTRY](HE_OBJECT_ENTRY.md) | `LONG_BLOB_ID` |
| [HE_SESSION](HE_SESSION.md) | `LONG_BLOB_ID` |
| [INVTN_COMMUNICATION](INVTN_COMMUNICATION.md) | `CONTENT_BLOB_ID` |
| [NURSING_ENCNTR_SCRATCHPAD](NURSING_ENCNTR_SCRATCHPAD.md) | `LONG_BLOB_ID` |
| [ORM_ERROR_LOG](ORM_ERROR_LOG.md) | `REQUEST_LONG_BLOB_ID` |
| [PAT_ED_DOC_ACTIVITY](PAT_ED_DOC_ACTIVITY.md) | `LONG_TEXT_ID` |
| [PDOC_AUTOSAVE](PDOC_AUTOSAVE.md) | `LONG_BLOB_ID` |
| [PDOC_TAG_TEXT](PDOC_TAG_TEXT.md) | `LONG_BLOB_ID` |
| [PL_ORG_LOGO_XREF](PL_ORG_LOGO_XREF.md) | `LONG_BLOB_ID` |
| [PROT_CRPC_BILLING](PROT_CRPC_BILLING.md) | `PROT_KCW_LONG_BLOB_ID` |
| [PROT_CRPC_BILLING](PROT_CRPC_BILLING.md) | `PROT_RPE_LONG_BLOB_ID` |
| [PW_PROCESSING_ACTION](PW_PROCESSING_ACTION.md) | `WORKFLOW_BLOB_ID` |
| [RX_CLAIM](RX_CLAIM.md) | `ATTACHMENT_BLOB_ID` |
| [SA_REF_ICON](SA_REF_ICON.md) | `LONG_BLOB_ID` |
| [SI_DOC_VALIDATION](SI_DOC_VALIDATION.md) | `VAL_INFO_BLOB_ID` |
| [SI_EPA_LOG](SI_EPA_LOG.md) | `LONG_BLOB_ID` |
| [SI_EPRESCRIBE_REQ_LOG](SI_EPRESCRIBE_REQ_LOG.md) | `LONG_BLOB_ID` |
| [SI_HAAD_FILE_DOWNLOAD](SI_HAAD_FILE_DOWNLOAD.md) | `FILE_CONTENT_ID` |
| [SN_COMMENT_TEXT](SN_COMMENT_TEXT.md) | `LONG_BLOB_ID` |
| [UCM_REPORT](UCM_REPORT.md) | `REPORT_RTF_ID` |
| [UCM_SPECIMEN_COMMENT](UCM_SPECIMEN_COMMENT.md) | `LONG_BLOB_ID` |

