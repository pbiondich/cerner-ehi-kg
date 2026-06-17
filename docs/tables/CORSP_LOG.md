# CORSP_LOG

> The corsp_log table stores information about both incoming and outgoing coorespondece. It holds the storage location of the correspondence and identifies any relationships with various other tables in the system.

**Description:** Correspondence Log  
**Table type:** ACTIVITY  
**Primary key:** `ACTIVITY_ID`  
**Columns:** 46  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_IND` | DOUBLE |  |  | Indicates whether this Correspondence is related to an account - No longer used |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ACTIVITY_ID` | DOUBLE | NOT NULL | PK FK→ | Unique Identifier and Foreign Key to the Activity Log table |
| 7 | `ACTIVITY_IND` | DOUBLE |  |  | Tells us to look on the Act_Act_Reltn table if 1 - No longer used |
| 8 | `ADDRESS_UPDATE_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the update types for the returned mail. |
| 9 | `BAD_ADDRESS_CD` | DOUBLE | NOT NULL |  | Stores the bad address type for the returned mail. |
| 10 | `BATCH_IND` | DOUBLE |  |  | Identifies whether a relationships exists. It cuts down the number of joins we have to perform by telling us whether we have a relationship to begin with - No longer used |
| 11 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 12 | `BILLING_ENTITY_IND` | DOUBLE |  |  | Tells us to look on the Corsp_BE_Reltn table if 1 - No longer used |
| 13 | `BILL_REC_IND` | DOUBLE |  |  | Indicates that a comment is related to a bill record - No longer used |
| 14 | `CORSP_DESC` | VARCHAR(250) |  |  | A memo field that summarizes the contents of the correspondence. |
| 15 | `CORSP_IND` | DOUBLE |  |  | Identifies whether a relationships exists. It cuts down the number of joins we have to perform by telling us whether we have a relationship to begin with - No longer used |
| 16 | `CORSP_STATUS_CD` | DOUBLE | NOT NULL |  | The status documents where the correspondence is in the process of being delivered to the recipient. |
| 17 | `CORSP_SUBJECT` | VARCHAR(100) |  |  | Free Text Subject field |
| 18 | `CORSP_SUBJECT_KEY` | VARCHAR(250) |  |  | Key Field for the Corsp_subect_key. This field can be indexed. |
| 19 | `CORSP_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the exact type of correspondence as a sub type of the Corsp_Type_CD |
| 20 | `CORSP_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of correspondence (Incoming, Outgoing, Comment) |
| 21 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 22 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the person that created the record. |
| 23 | `DELIVERED_DT_TM` | DATETIME |  |  | The date this correspondence was submitted to the external system responsible for delivery. |
| 24 | `DPV_CD` | DOUBLE | NOT NULL |  | Stores the delivery point validation status for the mail. |
| 25 | `ENCNTR_IND` | DOUBLE |  |  | Identifies whether a relationships exists. It cuts down the number of joins we have to perform by telling us whether we have a relationship to begin with - No longer used |
| 26 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 27 | `EXTERNAL_IDENT` | VARCHAR(250) |  |  | The external identifier is used primarily in the case of correspondence, which is transmitted to the Transaction Services hub. |
| 28 | `HEALTH_PLAN_IND` | DOUBLE |  |  | Identifies whether a relationships exists. It cuts down the number of joins we have to perform by telling us whether we have a relationship to begin with - No longer used |
| 29 | `IMPORTANCE_FLAG` | DOUBLE |  |  | Indicates the priority of a comment (i.e. Low, Medium, High) |
| 30 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the long_text table. |
| 31 | `MOVE_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the move type for the returned mail. |
| 32 | `ORGANIZATION_IND` | DOUBLE |  |  | Identifies whether a relationships exists. It cuts down the number of joins we have to perform by telling us whether we have a relationship to begin with - No longer used |
| 33 | `PERSON_IND` | DOUBLE |  |  | Identifies whether a relationships exists. It cuts down the number of joins we have to perform by telling us whether we have a relationship to begin with - No longer used |
| 34 | `PRSNL_IND` | DOUBLE |  |  | Identifies whether a relationships exists. It cuts down the number of joins we have to perform by telling us whether we have a relationship to begin with - No longer used |
| 35 | `REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason why the correspondence was posted. |
| 36 | `SESSION_IND` | DOUBLE |  |  | Identifies whether a relationships exists. It cuts down the number of joins we have to perform by telling us whether we have a relationship to begin with - No longer used |
| 37 | `STORAGE_LOC` | VARCHAR(100) |  |  | List the location of the stored correspondence (network path, filling system id's) |
| 38 | `STORAGE_TYPE_CD` | DOUBLE | NOT NULL |  | Describes how the correspondence is stored (network drive, filling cabinet, archived). |
| 39 | `SUBMITTED_DT_TM` | DATETIME |  |  | The date this correspondence was delivered. |
| 40 | `TRANS_IND` | DOUBLE |  |  | Identifies whether a relationships exists. It cuts down the number of joins we have to perform by telling us whether we have a relationship to begin with - No longer used |
| 41 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `WORKFLOW_CATEGORY_CD` | DOUBLE |  |  | Feild that holds the value of workflow model type. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_ID` | [ACTIVITY_LOG](ACTIVITY_LOG.md) | `ACTIVITY_ID` |
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CORSP_BR_RELTN](CORSP_BR_RELTN.md) | `ACTIVITY_ID` |
| [CORSP_KEYWORD_RELTN](CORSP_KEYWORD_RELTN.md) | `ACTIVITY_ID` |
| [CORSP_LOG_RELTN](CORSP_LOG_RELTN.md) | `ACTIVITY_ID` |
| [DEPOSIT_RECORD](DEPOSIT_RECORD.md) | `ACTIVITY_ID` |

