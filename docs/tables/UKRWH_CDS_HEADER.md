# UKRWH_CDS_HEADER

> Contains details common to CDS events.

**Description:** UK Reporting Warehouse Commissioning Data Set Header  
**Table type:** ACTIVITY  
**Primary key:** `UKRWH_CDS_HEADER_KEY`  
**Columns:** 115  
**Referenced by:** 10 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDRESS_FORMAT_NHS` | VARCHAR(2) |  |  | A code to determine the format of the associated PATIENT USUAL ADDRESS data. |
| 2 | `ADMINISTRATIVE_CATEGORY_NHS` | VARCHAR(2) |  |  | Identifies if a PATIENT is required to pay for treatment provided within a particular ACTIVITY or for transport. The same ADMINISTRATIVE CATEGORY will usually apply during the whole of a spell or episode but it may change, e.g. a PATIENT may start as an NHS patient, but then opt to change to a private patient. |
| 3 | `BIRTH_DT_TM` | DATETIME |  |  | The date on which a person was born or is officially deemed to have been born. |
| 4 | `CARER_SUPPORT_NHS` | VARCHAR(2) |  |  | An indication of whether or not carer support is available to the PATIENT at their normal residence. This does not include any paid support or support from a voluntary organisation, unless the PATIENT is normally resident in a Care Home. |
| 5 | `CDS_ACTIVITY_DT_TM` | DATETIME |  |  | Every CDS Type has a ""CDS Originating Date"" contained within the CDS data that must be used to populate the CDS ACTIVITY DATE. The CDS ACTIVITY DATE is held in the CDS Transaction Header Group and is a mandatory data element for all uses of the CDS for both Bulk Update and Net Change Protocols. |
| 6 | `CDS_APPLICABLE_DT_TM` | DATETIME |  |  | The date (with an associated CDS APPLICABLE TIME) of the update event (or the nearest equivalent) that resulted in the need to exchange this CDS. |
| 7 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 8 | `CDS_BULK_REPLACEMENT_GRP_NHS` | VARCHAR(3) | NOT NULL |  | The CDS Group into which CDS Types must be grouped when using the CDS Bulk Replacement Update Mechanism. |
| 9 | `CDS_COPY_RECIPIENT1_NACS` | VARCHAR(12) |  |  | CDS COPY RECIPIENT IDENTITY is the same as the attribute ORGANISATION CODE. The 5-character NHS ORGANISATION CODE (or valid default code) for an organisation indicated as a CDS COPY RECIPIENT IDENTITY of the CDS Message. |
| 10 | `CDS_COPY_RECIPIENT2_NACS` | VARCHAR(12) |  |  | CDS COPY RECIPIENT IDENTITY is the same as the attribute ORGANISATION CODE. The 5-character NHS ORGANISATION CODE (or valid default code) for an organisation indicated as a CDS COPY RECIPIENT IDENTITY of the CDS Message. |
| 11 | `CDS_COPY_RECIPIENT3_NACS` | VARCHAR(12) |  |  | CDS COPY RECIPIENT IDENTITY is the same as the attribute ORGANISATION CODE. The 5-character NHS ORGANISATION CODE (or valid default code) for an organisation indicated as a CDS COPY RECIPIENT IDENTITY of the CDS Message. |
| 12 | `CDS_COPY_RECIPIENT4_NACS` | VARCHAR(12) |  |  | CDS COPY RECIPIENT IDENTITY is the same as the attribute ORGANISATION CODE. The 5-character NHS ORGANISATION CODE (or valid default code) for an organisation indicated as a CDS COPY RECIPIENT IDENTITY of the CDS Message. |
| 13 | `CDS_COPY_RECIPIENT5_NACS` | VARCHAR(12) |  |  | CDS COPY RECIPIENT IDENTITY is the same as the attribute ORGANISATION CODE. The 5-character NHS ORGANISATION CODE (or valid default code) for an organisation indicated as a CDS COPY RECIPIENT IDENTITY of the CDS Message. |
| 14 | `CDS_COPY_RECIPIENT6_NACS` | VARCHAR(12) |  |  | CDS COPY RECIPIENT IDENTITY is the same as the attribute ORGANISATION CODE. The 5-character NHS ORGANISATION CODE (or valid default code) for an organisation indicated as a CDS COPY RECIPIENT IDENTITY of the CDS Message. |
| 15 | `CDS_COPY_RECIPIENT7_NACS` | VARCHAR(12) |  |  | CDS COPY RECIPIENT IDENTITY is the same as the attribute ORGANISATION CODE. The 5-character NHS ORGANISATION CODE (or valid default code) for an organisation indicated as a CDS COPY RECIPIENT IDENTITY of the CDS Message. |
| 16 | `CDS_EXTRACT_DT_TM` | DATETIME |  |  | The date & time (with an associated CDS EXTRACT TIME ) of the update event (or the nearest equivalent) that resulted in the need to exchange this CDS. |
| 17 | `CDS_PRIMARY_RECIPIENT_NACS` | VARCHAR(12) |  |  | CDS PRIME RECIPIENT IDENTITY is the same as the attribute ORGANISATION CODE. This is a mandatory 5-character NHS Organisation Code (or valid default code) representing the organisation determined to be the CDS PRIME RECIPIENT of the CDS Message as indicated in the CDS Addressing Grid detailed in the Commissioning Data Set Overview. |
| 18 | `CDS_PROTOCOL_NHS` | VARCHAR(3) |  |  | A code to identify the CDS Exchange Protocol and Update Mechanism associated with the transaction. |
| 19 | `CDS_RECORD_TYPE_NHS` | VARCHAR(3) | NOT NULL |  | A code to identify the specific type of Commissioning Data Set data. |
| 20 | `CDS_SENDER_NACS` | VARCHAR(12) |  |  | This is the identity of the ORGANISATION acting as the Sender of a CDS submission and is represented by that Organisation's ORGANISATION CODE. |
| 21 | `CDS_TEST_IND_TXT` | VARCHAR(1) | NOT NULL |  | This optional data item enables the individual CDS message to be classified as a normal or a test transaction. |
| 22 | `CDS_UNIQUE_IDENT` | VARCHAR(35) |  |  | When exchanging Commissioning Data Set data, this is an optional data element and when used is a unique number generated by the sender and inserted into the Commissioning Data Set data to enable senders and recipients to be able to cross-match and uniquely identify each and every Commissioning Data Set record. |
| 23 | `CDS_UPDATE_DEL_FLG` | DOUBLE |  |  | A code to indicate the required database update process for the submitted CDS Message. |
| 24 | `CDS_UPDT_DT_TM` | DATETIME |  |  | The date and time the CDS was last updated. |
| 25 | `COMMISSIONER_ORG_NACS` | VARCHAR(12) |  |  | This is the ORGANISATION CODE of the ORGANISATION commissioning health care. This should always be the ORGANISATION CODE of the original commissioner for Commissioning Data Sets to support Payment by Results. |
| 26 | `COMMISSIONER_REF_IDENT` | VARCHAR(17) |  |  | A number (alphanumeric) allocated by the commissioner to a REFERRAL REQUEST. |
| 27 | `COMMISSIONING_SERIAL_NBR_IDENT` | VARCHAR(6) |  |  | A number used to uniquely identify a NHS SERVICE AGREEMENT by an ORGANISATION acting as commissioner of patient care services. |
| 28 | `CONSULTANT_IDENT` | VARCHAR(8) |  |  | This is the GENERAL MEDICAL COUNCIL (GMC) NUMBER for the CONSULTANT. For GENERAL MEDICAL PRACTITIONERS working as CONSULTANTS, the GENERAL MEDICAL PRACTITIONER's GENERAL MEDICAL COUNCIL (GMC) NUMBER should be used, see data item note for GENERAL MEDICAL PRACTITIONER (SPECIFIED). |
| 29 | `DIRECT_ACCESS_REFERRAL_IND_NHS` | VARCHAR(1) |  |  | An indication of whether a PATIENT was referred to a Direct Access Service. |
| 30 | `EARLIEST_RSNBL_OFFER_DT_TM` | DATETIME |  |  | It is the date of the earliest of the reasonable offers made to a patient for an appointment or elective admission. it should only be included on the commissioning data sets where the patient has declined at least two reasonable offers. |
| 31 | `EC_ACCESS_INFO_PROF_REQ_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify that the patient requires support from a communication professional. |
| 32 | `EC_ACCOMMODATION_STATUS_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify the details of the accommodation of the person. |
| 33 | `EC_INTERPRETER_LANGUAGE_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to record the language of the interpreter required by the person. |
| 34 | `EC_OVERSEAS_VIST_CHRG_CATG_NHS` | VARCHAR(1) |  |  | The charging category relating to an overseas visitor status recorded at the cds activity date. |
| 35 | `EC_PERSON_STATED_GENDER_CD_NHS` | VARCHAR(1) |  |  | The self declared or inferred by observation for those unable to declare their person stated gender. |
| 36 | `EC_PREFERRED_SPOKEN_LANG_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to capture the preferred spoken language of the person. |
| 37 | `ETHNIC_CATEGORY_2021_NHS` | VARCHAR(3) |  |  | The ethnicity of a PERSON, as specified by the PERSON using classification code used for the 2021 census. |
| 38 | `ETHNIC_CATEGORY_NHS` | VARCHAR(2) |  |  | The ethnicity of a PERSON, as specified by the PERSON. |
| 39 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 40 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 41 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 42 | `HRG_DRGVP_TXT` | VARCHAR(4) |  |  | HRG DOMINANT GROUPING VARIABLE-PROCEDURES is a field derived by the Healthcare Resource Group Acute Inpatient Grouper. It represents the procedure that the Healthcare Resource Group grouping algorithm has identified as having the greatest effect upon the resources consumed by a PATIENT. It is required for the production of the National Schedule of Reference Costs reports. |
| 43 | `HRG_PROCEDURE_SCHEME_TXT` | VARCHAR(2) |  |  | This is used in the Clinical Activity Group of the CDS to denote the scheme basis of an Intervention Operation or A&E Treatment |
| 44 | `HRG_TXT` | VARCHAR(3) |  |  | This is the HRG Code |
| 45 | `HRG_VERSION_NBR_NHS` | VARCHAR(3) |  |  | HEALTHCARE RESOURCE GROUP CODE-VERSION NUMBERS identify which version of the Healthcare Resource Group has been used to identify the Healthcare Resource Group. |
| 46 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 47 | `LEAD_CARE_ACTIVITY_NHS` | VARCHAR(1) |  |  | An indicator that the first PERSON in the PERSON RELATIONSHIP is a lead contact to the second PERSON. That is the PERSON acting as a lead contact or proxy for the other PERSON, in circumstances where the second PERSON is unable to communicate effectively or lacks the capacity to make medical decisions and the proxy is authorised to act for that PERSON. This may be the case if the PERSON requiring a lead contact is an infant, has a disability or has an illness preventing direct communication. |
| 48 | `LINE1_ADDR` | VARCHAR(35) |  |  | The first text string comprising one line of an ADDRESS. |
| 49 | `LINE2_ADDR` | VARCHAR(35) |  |  | The second text string comprising one line of an ADDRESS. |
| 50 | `LINE3_ADDR` | VARCHAR(35) |  |  | The third text string comprising one line of an ADDRESS. |
| 51 | `LINE4_ADDR` | VARCHAR(35) |  |  | The fourth text string comprising one line of an ADDRESS. |
| 52 | `LINE5_ADDR` | VARCHAR(35) |  |  | The fifth text string comprising one line of an ADDRESS. |
| 53 | `LOCAL_PATIENT_IDENT` | VARCHAR(10) |  |  | An identifier, other than a name, which identifies a PERSON. |
| 54 | `LOCAL_PATIENT_ID_ORG_NACS` | VARCHAR(12) |  |  | This is the identification of a PATIENT having a relationship with a particular ORGANISATION such as a PATIENT having been registered with a Trust for SERVICES. |
| 55 | `LOCAL_SPECIALTY_NHS` | VARCHAR(3) |  |  | A local code identifying each local specialty designated by the NHS organisation. These are usually related to main specialty codes. |
| 56 | `LOCAL_SUBSPECIALTY_NHS` | VARCHAR(8) |  |  | A local code identifying each local sub-specialty designated by the NHS organisation. These are usually related to local specialty codes. |
| 57 | `LOC_EARLIEST_RSNBL_OFFER_DT_TM` | DATETIME |  |  | It is the date of the earliest of the reasonable offers made to a patient for an appointment or elective admission. it should only be included on the commissioning data sets where the patient has declined at least two reasonable offers. |
| 58 | `MAIN_SPECIALTY_NHS` | VARCHAR(3) |  |  | A unique code identifying each main specialty designated by Royal Colleges. This is the same as the occupation codes describing specialties. |
| 59 | `MARITAL_STATUS_NHS` | VARCHAR(1) |  |  | An indicator to identify the legal marital status of a PERSON. |
| 60 | `NAME_FORMAT_NHS` | VARCHAR(2) |  |  | This is used in the CDS to identify the format of a PATIENT NAME, with the classification values indicating whether it is a PERSON NAME STRUCTURED or PERSON NAME UNSTRUCTURED. |
| 61 | `NHS_NBR_IDENT` | VARCHAR(10) |  |  | A number used to identify a person uniquely within the NHS in England and Wales. This field contains the NHS Number of the patient, which is the primary identifier of a person registered for health care; it is unique. Records for babies under six weeks of age and for patients admitted through accident and emergency tend to have null entries for this field. |
| 62 | `NHS_NBR_STATUS_NHS` | VARCHAR(2) |  |  | Codes in this field indicate whether the patients' NHS Number is present, and if it is verified. If the NHS Number is absent, the indicator gives the reason why. |
| 63 | `NHS_SRVC_AGREEMENT_LINE_IDENT` | VARCHAR(10) |  |  | A number used to uniquely identify a NHS SERVICE AGREEMENT by an ORGANISATION acting as commissioner of patient care services. |
| 64 | `OVERSEAS_VISITOR_STATUS_NHS` | VARCHAR(1) |  |  | The status of a PATIENT who is an Overseas Visitor |
| 65 | `OVERSEAS_VISITOR_STATUS_NHS_2` | VARCHAR(1) |  |  | The status of a PATIENT who is an Overseas Visitor |
| 66 | `OVERSEAS_VISITOR_STATUS_NHS_3` | VARCHAR(1) |  |  | The status of a PATIENT who is an Overseas Visitor |
| 67 | `OVERSEAS_VISITOR_STATUS_NHS_4` | VARCHAR(1) |  |  | The status of a PATIENT who is an Overseas Visitor |
| 68 | `OVERSEAS_VISITOR_STATUS_NHS_5` | VARCHAR(1) |  |  | The status of a PATIENT who is an Overseas Visitor |
| 69 | `OVERSEAS_VS_END_DT_TM` | DATETIME |  |  | The end datetime of patient's Overseas Visitor status |
| 70 | `OVERSEAS_VS_END_DT_TM_2` | DATETIME |  |  | The end datetime of patient's Overseas Visitor status |
| 71 | `OVERSEAS_VS_END_DT_TM_3` | DATETIME |  |  | The end datetime of patient's Overseas Visitor status |
| 72 | `OVERSEAS_VS_END_DT_TM_4` | DATETIME |  |  | The end datetime of patient's Overseas Visitor status |
| 73 | `OVERSEAS_VS_END_DT_TM_5` | DATETIME |  |  | The end datetime of patient's Overseas Visitor status |
| 74 | `OVERSEAS_VS_START_DT_TM` | DATETIME |  |  | The start datetime of patient's Overseas Visitor status |
| 75 | `OVERSEAS_VS_START_DT_TM_2` | DATETIME |  |  | The start datetime of patient's Overseas Visitor status |
| 76 | `OVERSEAS_VS_START_DT_TM_3` | DATETIME |  |  | The start datetime of patient's Overseas Visitor status |
| 77 | `OVERSEAS_VS_START_DT_TM_4` | DATETIME |  |  | The start datetime of patient's Overseas Visitor status |
| 78 | `OVERSEAS_VS_START_DT_TM_5` | DATETIME |  |  | The start datetime of patient's Overseas Visitor status |
| 79 | `PATIENT_FORENAME` | VARCHAR(35) |  |  | The specific first name of a patient by which a PERSON may be known. |
| 80 | `PATIENT_FULL_NAME` | VARCHAR(70) |  |  | Patient's first and last name |
| 81 | `PATIENT_INITIALS` | VARCHAR(35) |  |  | Patient Initials |
| 82 | `PATIENT_NAME_SUFFIX` | VARCHAR(35) |  |  | Patient Suffix |
| 83 | `PATIENT_PATHWAY_IDENT` | VARCHAR(20) |  |  | An identifier, which together with the ORGANISATION CODE of the issuer, uniquely identifies a PATIENT PATHWAY. |
| 84 | `PATIENT_PATHWAY_ISSUER_NACS` | VARCHAR(12) |  |  | The ORGANISATION CODE of the issuer, which is used to uniquely identify a PATIENT PATHWAY. |
| 85 | `PATIENT_REQUESTED_NAME` | VARCHAR(70) |  |  | Patient's requested name |
| 86 | `PATIENT_SURNAME` | VARCHAR(35) |  |  | The specific surname / last name of a patient by which a PERSON may be known. |
| 87 | `PATIENT_TITLE` | VARCHAR(35) |  |  | Patient's title |
| 88 | `PATIENT_UNSTRUCTURED_ADDRESS` | VARCHAR(175) |  |  | Patient's full unstructured address |
| 89 | `PCT_RESIDENCE_NACS` | VARCHAR(12) |  |  | The Organisation code of the responsible commissioner for a specific geographic area where PATIENTS not registered with a General Medical Practitioner Practice but resident in the GEOGRAPHIC AREA covered by a Primary Care Trust are the responsibility of that Primary Care Trust. The National Administrative Codes Service provides postcode files which link postcodes to PCT OF RESIDENCES. |
| 90 | `POSTCODE` | VARCHAR(25) |  |  | The code allocated by the Post Office to identify a group of postal delivery points. A code used primarily for the delivery of correspondence to ADDRESSES. POSTCODES may also be used to define a GEOGRAPHIC AREA. |
| 91 | `PROVIDER_ORG_NACS` | VARCHAR(12) |  |  | An ORGANISATION providing patient care services within a NHS SERVICE AGREEMENT. |
| 92 | `PROVIDER_REF_IDENT` | VARCHAR(17) |  |  | A convention agreed locally between a provider and Commissioner for use within a CDS message. |
| 93 | `PT_AGE_AT_ACTIVITY_YEARS` | DOUBLE |  |  | This is derived as the number of completed years between the PERSON BIRTH DATE of the PATIENT and the ATTENDANCE DATE or the estimated age of the PATIENT. |
| 94 | `REFERRER_IDENT` | VARCHAR(8) |  |  | This requires the code of the PERSON making the referral. This will normally be a CARE PROFESSIONAL - a GENERAL MEDICAL PRACTITIONER or a CONSULTANT. |
| 95 | `REFERRER_ORG_NACS` | VARCHAR(12) |  |  | This is the ORGANISATION CODE of the ORGANISATION from which the referral is made, such as GP Practice or NHS Trust. This information is essential for managing service agreements which are based on patterns of referral. The National Cancer Waiting Times Monitoring Data Set (22/2002) does not require GP Practices and stipulates a maximum length of an5 to record the appropriate NHS Trust. |
| 96 | `REGISTERED_GMP_IDENT` | VARCHAR(8) |  |  | This is the code of the GENERAL MEDICAL PRACTITIONER specified by the PATIENT. |
| 97 | `REGISTERED_GP_PRCTC_ORG_NACS` | VARCHAR(12) |  |  | This is the code of the GP Practice that the PATIENT is registered with. |
| 98 | `RTT_PERIOD_END_DT_TM` | DATETIME |  |  | The end date of a REFERRAL TO TREATMENT PERIOD. |
| 99 | `RTT_PERIOD_START_DT_TM` | DATETIME |  |  | The start date of a REFERRAL TO TREATMENT PERIOD. |
| 100 | `RTT_PERIOD_STATUS_NHS` | VARCHAR(2) |  |  | The status of an ACTIVITY (or anticipated ACTIVITY) for the 18 week REFERRAL TO TREATMENT PERIOD decided by the lead CARE PROFESSIONAL. |
| 101 | `RTT_WAIT_TIME_MEAS_TYPE_NHS` | VARCHAR(2) |  |  | The type of waiting time measurement methodology which may be applied during a PATIENT PATHWAY. |
| 102 | `SECURITY_KEY` | DOUBLE |  |  | The identifier associated to the reference object selected for row-level security. |
| 103 | `SEX_CD_NHS` | VARCHAR(1) |  |  | SEX is the same as the attribute PERSON GENDER CODE. |
| 104 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 105 | `TREATMENT_FUNCTION_NHS` | VARCHAR(3) |  |  | This is the TREATMENT FUNCTION under which the PATIENT is treated. |
| 106 | `UBRN_IDENT` | VARCHAR(12) |  |  | The unique booking reference number assigned by the NHS Connecting for Health Choose and Book system when a PATIENT accepts an APPOINTMENT DATE OFFERED of an APPOINTMENT OFFER where the offer was made via the NHS Connecting for Health Choose and Book system. |
| 107 | `UKRWH_CDS_HEADER_KEY` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the ukrwh cds header table. It is an internal system assigned number. |
| 108 | `UKRWH_CDS_LOAD_KEY` | DOUBLE | NOT NULL |  | Uniquely identifies the load id related to this cds load. |
| 109 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 110 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 111 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 112 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 113 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 114 | `WITHHELD_FLG` | VARCHAR(1) |  |  | Indicates whether patient data has been anonymised |
| 115 | `WITHHELD_IDENTITY_REASON_NHS` | VARCHAR(2) |  |  | NHS values which identifys that the record has been purposely anonymised for a valid reason |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (10)

| From table | Column |
|------------|--------|
| [UKRWH_CDE_SCH_EVENT_ACTION](UKRWH_CDE_SCH_EVENT_ACTION.md) | `UKRWH_CDS_HEADER_KEY` |
| [UKRWH_CDS_AE_ATTENDANCE](UKRWH_CDS_AE_ATTENDANCE.md) | `UKRWH_CDS_HEADER_KEY` |
| [UKRWH_CDS_APC_EPISODE](UKRWH_CDS_APC_EPISODE.md) | `UKRWH_CDS_HEADER_KEY` |
| [UKRWH_CDS_DIAGNOSIS](UKRWH_CDS_DIAGNOSIS.md) | `UKRWH_CDS_HEADER_KEY` |
| [UKRWH_CDS_EAL_ENTRY](UKRWH_CDS_EAL_ENTRY.md) | `UKRWH_CDS_HEADER_KEY` |
| [UKRWH_CDS_EAL_OFFER](UKRWH_CDS_EAL_OFFER.md) | `UKRWH_HEADER_KEY` |
| [UKRWH_CDS_EAL_REMOVAL](UKRWH_CDS_EAL_REMOVAL.md) | `UKRWH_HEADER_KEY` |
| [UKRWH_CDS_EAL_SUSPENSION](UKRWH_CDS_EAL_SUSPENSION.md) | `UKRWH_HEADER_KEY` |
| [UKRWH_CDS_OP_ATTENDANCE](UKRWH_CDS_OP_ATTENDANCE.md) | `UKRWH_CDS_HEADER_KEY` |
| [UKRWH_CDS_PROCEDURE](UKRWH_CDS_PROCEDURE.md) | `UKRWH_CDS_HEADER_KEY` |

