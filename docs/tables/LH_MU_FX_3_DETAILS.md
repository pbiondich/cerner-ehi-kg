# LH_MU_FX_3_DETAILS

> This table holds the documented data for the encounter and person based measures

**Description:** LH_MU_FX_3_DETAILS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 60

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEDROCK_MASK_FLAG` | DOUBLE |  |  | The value is a bit mask used to store indicators about bedrock Yes/No filters during the load. |
| 3 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Unique value for each eligible provider coming from br_eligible_provider table |
| 4 | `CCD_SOURCE` | VARCHAR(50) |  |  | This column contains source of the Continuity of Care Document (CCD) |
| 5 | `CCD_SOURCE_IDENTIFIER_TEXT` | VARCHAR(125) |  |  | This column contains the source document unique identifier of a CCD document. |
| 6 | `CLIN_REC_ALLERGY_IND` | DOUBLE |  |  | Indicates if an allergy profile was reconciled |
| 7 | `CLIN_REC_CCDA_DT_TM` | DATETIME |  |  | The time that the CCDA document was attributed |
| 8 | `CLIN_REC_CCDA_IND` | DOUBLE |  |  | Indicates if there was a CCDA document associated |
| 9 | `CLIN_REC_MED_IND` | DOUBLE |  |  | Indicates if a medication list was reconciled |
| 10 | `CLIN_REC_PROB_IND` | DOUBLE |  |  | Indicates if ta problem list was reconciled |
| 11 | `DOC_ENCNTR_ID` | DOUBLE | NOT NULL |  | This column mentions the encounter id on whom the documentation is done. |
| 12 | `DOC_ENCNTR_ID_POS` | DOUBLE | NOT NULL |  | This column mentiones the pos value of the encounter on whom the documentation is done. POS values will either be 0,21,22,23. |
| 13 | `EP_CCN_FLAG` | DOUBLE |  |  | This column will have the values of 1 ( to indicate this is a ccn patient ) 2 (to indicate this is an ep patient) and 3 ( to indicate this is an ep22 patient) |
| 14 | `EVENT_DESCRIPTION` | VARCHAR(50) |  |  | Detailed description of the event |
| 15 | `EVENT_DT_TM` | DATETIME |  |  | Date and time for the event ( clinical_event/ order_action_dt_tm etc) |
| 16 | `EVENT_LOC_DT_TM` | DATETIME |  |  | The local version of the EVENT_DT_TM column. |
| 17 | `EXTRACT_DT_TM` | DATETIME |  |  | Date and time when the row was extracted |
| 18 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 19 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 20 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 21 | `HIE_ASK_NO_RECV_IND` | DOUBLE |  |  | Indicates that summary of care was asked but not received for the encounter. |
| 22 | `HIE_CCD_DOCUMENT_DT_TM` | DATETIME |  |  | Date and time when the CCD Document was generated. |
| 23 | `HIE_CCD_DOCUMENT_ID` | DOUBLE | NOT NULL |  | CCD Document Id for HIE. |
| 24 | `HIE_CCD_DOCUMENT_LOC_DT_TM` | DATETIME |  |  | The local version of the HIE_CCD_DOCUMENT_DT_TM column. |
| 25 | `HIE_DENOM_SOURCE` | VARCHAR(50) |  |  | The name of the source that qualified the encounter to be part of the denominator. |
| 26 | `HIE_DENOM_TEXT` | VARCHAR(200) |  |  | The text value corresponding to the id or cd in denom_value. |
| 27 | `HIE_DENOM_VALUE` | DOUBLE |  |  | The value corresponding to the denom source, either an ID or a code value. |
| 28 | `HIE_NO_DATA_IND` | DOUBLE |  |  | Indicates if the encounter has a clinical event associated with the 'Queried an external HIE no Data found' Bedrock filter. |
| 29 | `HIE_NO_HIE_IND` | DOUBLE |  |  | Indicates if the 'No HIE available' Bedrock filter is set to 'YES'. |
| 30 | `HIE_PAT_FLAG` | DOUBLE |  |  | Describes the type of encounter where 1 is NEW, 2 is REF, and 3 is CCD. |
| 31 | `HIE_SUM_VIEWED_IND` | DOUBLE |  |  | Indicates if the encounter has a clinical event associated with the 'Summary of Care viewed' Bedrock filter. |
| 32 | `HIE_XDOC_IND` | DOUBLE |  |  | Indicates if encounter has a document in the SI_XDOC_METADATA table. |
| 33 | `HIE_XDS_QUERIED_IND` | DOUBLE |  |  | Indicates if encounter has a row on the SI_XDOC_QUERY_PERSON_RELTN table. |
| 34 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 35 | `LH_MU_FX_3_DETAILS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_MU_FX_3_DETAILS table. |
| 36 | `LH_MU_FX_3_POP_METRICS_ID` | DOUBLE | NOT NULL | FK→ | Foreign key column, coming from lh_mu_fx_3_pop_metrics table |
| 37 | `METRIC_TYPE` | VARCHAR(50) |  |  | Measure mean |
| 38 | `MSG_POOL_NAME` | VARCHAR(100) |  |  | The column stores the name of the pool, the message was sent from. The value stored is prsnl_group_name from prsnl_group table. |
| 39 | `NUMERATOR_IND` | DOUBLE |  |  | Indicates if the row qualifies for MET OUTCOME |
| 40 | `OUTCOME_DETAIL` | VARCHAR(250) |  |  | Reason for the outcome |
| 41 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Will contain the primary key of the tables for which the row qualified |
| 42 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | Contains the name of the table for which the row qualifies |
| 43 | `PORTAL_ACCESS_IND` | DOUBLE | NOT NULL |  | This column indicates if the person was offered portal access. |
| 44 | `PORTAL_ACCOUNT_IND` | DOUBLE | NOT NULL |  | This column indicates if the person has a portal account created. |
| 45 | `QUERY_MEAN` | VARCHAR(50) |  |  | Name of the query |
| 46 | `SEC_MSG_EP_TYPE_FLAG` | DOUBLE |  |  | Status whether the provider on the br_eligible_provider_d column was listed on the TOC or CC field of the message. This will have 3 values ( 1,2,3)1 if the provider is in the cc section of the message2 if the provider is in the to section of the message3 if the provider_id corresponds to the eligible/responsible provider |
| 47 | `SEC_MSG_NOTE_TYPE_TEXT` | VARCHAR(50) |  |  | The type of message |
| 48 | `SEC_MSG_SENDER_ID` | DOUBLE | NOT NULL |  | The provider ID of provider who sent the message |
| 49 | `SUB_METRIC_TYPE` | VARCHAR(50) |  |  | More information for the respective metric type |
| 50 | `TOC_ALLERGY_IND` | DOUBLE |  |  | Indicates the allergy documented for TOC |
| 51 | `TOC_MED_IND` | DOUBLE |  |  | Indicates the medication documented for TOC |
| 52 | `TOC_PROB_IND` | DOUBLE |  |  | Indicates the problems documented for TOC |
| 53 | `TOC_PROB_SNOMED_IND` | DOUBLE |  |  | Indicates if the documented problem id SNOMED or not for TOC |
| 54 | `TOC_RECIPIENT_TYPE` | VARCHAR(50) |  |  | Different ways in which CCD Document will be sent ( EMAIL, PUBLISH, PRINT, FAX). |
| 55 | `TOC_REF_PROV_FREETEXT` | VARCHAR(255) |  |  | Provider names entered in the freetext field while referring the referral order to a Provider. Value coming from Order detail table where field meaning is REFERREDTOFREETXTPROVIDER. |
| 56 | `TOC_REF_TO_PROV` | VARCHAR(255) |  |  | Provider who the referral order is referred to while placing a referral order . Value coming from Order detail table where field meaning is REFERREDTOPROVIDER. |
| 57 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 58 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 59 | `UPDT_SOURCE` | VARCHAR(50) |  |  | Source which updated the row |
| 60 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_MU_FX_3_POP_METRICS](LH_MU_FX_3_POP_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_MU_FX_3_POP_METRICS_ID` | [LH_MU_FX_3_POP_METRICS](LH_MU_FX_3_POP_METRICS.md) | `LH_MU_FX_3_POP_METRICS_ID` |

