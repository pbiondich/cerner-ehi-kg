# UKRWH_CDS_RTT_EVENT

> Contains Referral to Treatment details relatign to CDS events as well as detaisl relating to non CDS administrative event.

**Description:** UK Reporting Warehouse Commissioning Data Set Refferal To Treatment Event  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 49

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME |  |  | Any date or time that is pertinent to an ACTIVITY. |
| 2 | `ADC_COMMENTS` | VARCHAR(255) |  |  | This is the value of the comments recorded on the RTT Powerform |
| 3 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 4 | `CDS_RECORD_TYPE_NHS` | VARCHAR(3) |  |  | A code to identify the specific type of Commissioning Data Set data. |
| 5 | `DECEASED_DT_TM` | DATETIME |  |  | The date on which a PERSON died or is officially deemed to have died. |
| 6 | `ENCOUNTER_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 7 | `EPISODE_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the episode table. It is an internal system assigned number. |
| 8 | `EXTRACT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was extracted. |
| 9 | `FIN_IDENT` | VARCHAR(12) |  |  | This is the value of the unique primary identifier of the encounter financial table. It is an internal system assigned number. |
| 10 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 11 | `GP_PRACTICE_ORG` | VARCHAR(40) |  |  | The Millennium organization identifier for a GP Practice. |
| 12 | `GP_PRSNL` | VARCHAR(40) |  |  | The Millennium Personnel Identifier for GP |
| 13 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 14 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 15 | `ITT_RTT_START_DT_TM` | DATETIME |  |  | The start date of a REFERRAL TO TREATMENT PERIOD from an Inter Trust Transfer |
| 16 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 17 | `LOCAL_PATIENT_IDENT` | VARCHAR(10) |  |  | An identifier, other than a name, which identifies a PERSON. |
| 18 | `LOC_ACTIVITY_DT_TM` | DATETIME |  |  | Any date or time that is pertinent to an activity. |
| 19 | `LOC_ITT_RTT_START_DT_TM` | DATETIME |  |  | The start date of a referral to treatment period from an inter trust transfer. |
| 20 | `LOC_RTT_EVENT_DT_TM` | DATETIME |  |  | The applicable effective date time of an rtt event. |
| 21 | `MAIN_SPECIALTY_REF` | VARCHAR(40) |  |  | The Millennium code identifier for the main specialty code of the responsible health care provider |
| 22 | `NHS_NBR_IDENT` | VARCHAR(10) |  |  | A number used to identify a person uniquely within the NHS in England and Wales. This field contains the NHS Number of the patient, which is the primary identifier of a person registered for health care; it is unique. Records for babies under six weeks of age and for patients admitted through accident and emergency tend to have null entries for this field. |
| 23 | `OUTCOME_NHS` | VARCHAR(2) |  |  | This field contains the outcome of the RTT event |
| 24 | `PARENT_ENTITY_NAME` | VARCHAR(30) |  |  | This is the value of the parent entity name on the Millennium CDS_BATCH_CONTENT table |
| 25 | `PARENT_ENTITY_SK` | VARCHAR(40) |  |  | This is the value of the parent entity id on the Millennium CDS_BATCH_CONTENT table |
| 26 | `PATIENT_PATHWAY_IDENT` | VARCHAR(20) |  |  | An identifier, which together with the ORGANISATION CODE of the issuer, uniquely identifies a PATIENT PATHWAY. |
| 27 | `PATIENT_PATHWAY_ISSUER_NACS` | VARCHAR(6) |  |  | The ORGANISATION CODE of the issuer, which is used to uniquely identify a PATIENT PATHWAY. |
| 28 | `PERSON_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 29 | `PROVIDER_ORG_NACS` | VARCHAR(5) |  |  | An ORGANISATION providing patient care services within a NHS SERVICE AGREEMENT. |
| 30 | `RESPONSIBLE_HCP_PRSNL` | VARCHAR(40) |  |  | The Millennium Personnel Identifier for HCP |
| 31 | `RTT_EVENT_DT_TM` | DATETIME |  |  | The applicable effective date time of an rtt event. |
| 32 | `RTT_EVENT_UNIQUE_ID` | VARCHAR(35) |  |  | This is the unique identifier for the RTT event |
| 33 | `RTT_PERIOD_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique identifier of the UKRWH_CDS_RTT_PERIOD table. It is an internal system assigned number |
| 34 | `RTT_PERIOD_STATUS` | VARCHAR(10) |  |  | The interpretation of the rtt event status. e.g. START, STOP, OTHER |
| 35 | `RTT_REF` | VARCHAR(40) |  |  | This is the value of the Millennium Code Value for the RTT Status |
| 36 | `RTT_START_DT_TM` | DATETIME |  |  | The start date of a REFERRAL TO TREATMENT PERIOD. |
| 37 | `RTT_STATUS_NHS` | VARCHAR(2) |  |  | The status of an ACTIVITY (or anticipated ACTIVITY) for the 18 week REFERRAL TO TREATMENT PERIOD decided by the lead CARE PROFESSIONAL. |
| 38 | `RTT_STOP_DT_TM` | DATETIME |  |  | The end date of a REFERRAL TO TREATMENT PERIOD. |
| 39 | `RTT_UPDATE_DEL_FLG` | DOUBLE |  |  | This field contains the count of the number of times the record has been marked for update / deletion |
| 40 | `SUSPENSION_REASON_TXT` | VARCHAR(100) |  |  | A period of time during which a PATIENT with an ELECTIVE ADMISSION LIST ENTRY on an ELECTIVE ADMISSION LIST is unavailable for admission due to medical or PATIENT initiated reasons and therefore should not be given an OFFER OF ADMISSION for that interval. |
| 41 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 42 | `TREATMENT_FUNCTION_REF` | VARCHAR(40) |  |  | The Millennium code identifier for the treatment function code of the responsible health care provider |
| 43 | `UKRWH_CDS_HEADER_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cds header table. It is an internal system assigned number. |
| 44 | `UKRWH_CDS_RTT_EVENT_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cds rtt event table. It is an internal system assigned number. |
| 45 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 46 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

