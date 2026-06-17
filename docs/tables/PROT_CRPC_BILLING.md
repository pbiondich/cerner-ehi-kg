# PROT_CRPC_BILLING

> Information on the XML files generated for Clinical Research Process Content and Knowledge Compiler Wizard.

**Description:** PROTOCOL CLINICAL RESEARCH PROCESS CONTENT BILLING  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `PROT_CRPC_BILLING_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `PROT_FILE_NAME` | VARCHAR(200) | NOT NULL |  | The name of the file. For protocol's it will be the protocol title and for arm's it will be a combination of protocol title and arm title. |
| 5 | `PROT_FILE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Protocol File Type Flag: 1 = PROT1OCOL; 2 = ARM |
| 6 | `PROT_KCW_LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The ID of the Retrieve Protocol for Execution(RPE) XML file stored on the long_blob table. |
| 7 | `PROT_KCW_PROCESS_STATUS_IND` | DOUBLE | NOT NULL |  | The Success/Failure indicator to represent the status of the incoming Clinical Research Process Content(CRPC) request to Knowledge Compiler Wizard(KCW) compatible XML conversion. |
| 8 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the PROT_MASTER table |
| 9 | `PROT_POWER_PLAN_CMNT_TXT` | VARCHAR(2000) |  |  | The comments user adds pertaining to the power plan that is being processed in the knowledge compiler wizard. |
| 10 | `PROT_POWER_PLAN_DT_TM` | DATETIME |  |  | The processing date of the power plan in knowledge compiler wizard. This value will be entered by the user. |
| 11 | `PROT_POWER_PLAN_NAME` | VARCHAR(255) |  |  | The name of the power plan. Entered by user. |
| 12 | `PROT_POWER_PLAN_STATUS_IND` | DOUBLE |  |  | The processing status indicator of the power plan. Selected by user after processing power plan in knowledge compiler wizard. This is not a boolean field, as the name might imply, but can contain multiple values. Valid values are: 0=not assigned, 1=Production, 2=Testing, 3=Archive, 4=Inactive |
| 13 | `PROT_REQ_UPDATE_CNT` | DOUBLE | NOT NULL |  | The count of updates that happened through web service requests |
| 14 | `PROT_REQ_UPDATE_DT_TM` | DATETIME |  |  | The date on which the update occurred through a web service request. |
| 15 | `PROT_RESEARCH_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | The id of the Research Account that is linked with the protocol |
| 16 | `PROT_RESEARCH_ACCOUNT_NAME` | VARCHAR(255) |  |  | The research account of the organization which is billed for the ongoing study protocol. |
| 17 | `PROT_RES_ACCNT_CD` | DOUBLE | NOT NULL | FK→ | represents the Research Account used for Clinical trials billing. (The code value from code set 4504006) |
| 18 | `PROT_RPE_LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The ID of the Knowledge Compiler Wizard(KCW) XML file stored on the long_blob table. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_STATUS_IND` | DOUBLE |  |  | Indicates whether the update request was processed successfully |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROT_KCW_LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |
| `PROT_RESEARCH_ACCOUNT_ID` | [RESEARCH_ACCOUNT](RESEARCH_ACCOUNT.md) | `RESEARCH_ACCOUNT_ID` |
| `PROT_RES_ACCNT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PROT_RPE_LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

