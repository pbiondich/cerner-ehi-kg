# PERSON_PATIENT_HIST

> Used for tracking history of certain columns on the person_patient table.

**Description:** Person Patient History Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 95

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADOPTED_CD` | DOUBLE | NOT NULL |  | Describes the adopted status of the person. |
| 6 | `ADVOCATE_REQUIRED_CD` | DOUBLE | NOT NULL |  | Identifies it the patient requires someone to be present to help them understand and make decisions around their clinical care. |
| 7 | `BAD_DEBT_CD` | DOUBLE | NOT NULL |  | Describes a level or status of bad debt risk represented by the person. |
| 8 | `BAPTISED_CD` | DOUBLE | NOT NULL |  | Describes the baptised status of the person |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `BIRTH_CERTIFICATE_IDENT` | VARCHAR(100) |  |  | The numeric or textual identifier of the government issued vital document which certifies the patient's birth. |
| 11 | `BIRTH_LENGTH` | DOUBLE |  |  | The numerical length of the person recorded at birth. |
| 12 | `BIRTH_LENGTH_UNITS_CD` | DOUBLE | NOT NULL |  | The units used to record the birth length. |
| 13 | `BIRTH_MULTIPLE_CD` | DOUBLE | NOT NULL |  | Identifies a birth of more than one baby (i.e., twins, triplets, etc. |
| 14 | `BIRTH_ORDER` | DOUBLE |  |  | In the case of a multiple birth, the number which represents the order of brith for the person. |
| 15 | `BIRTH_ORDER_CD` | DOUBLE | NOT NULL |  | In the case of a multiple birth, the number which represents the order of birth for the person. This is essentially the same information that is stored in column Birth_Order but the UK handles this field differently so this new column was needed to accomodate the UK processing. |
| 16 | `BIRTH_SEX_CD` | DOUBLE | NOT NULL |  | The sex, typically determined by biological characteristics such as reproductive anatomy or genetic makeup, assigned at birth for the purposes of birth registration. |
| 17 | `BIRTH_WEIGHT` | DOUBLE |  |  | The numerical weight of the person recorded at birth. |
| 18 | `BIRTH_WEIGHT_UNITS_CD` | DOUBLE | NOT NULL |  | The units used to record the birth weight. |
| 19 | `CALLBACK_CONSENT_CD` | DOUBLE | NOT NULL |  | Denotes if the person has provided their consent to be contacted. |
| 20 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 21 | `CHURCH_CD` | DOUBLE | NOT NULL |  | Identifies the specific church or place of worship with which the person is associated. |
| 22 | `CONTACT_FOR_RESEARCH_PERM_CD` | DOUBLE | NOT NULL |  | Information regarding if the patient has given permission to be contacted for research purposes |
| 23 | `CONTACT_LIST_CD` | DOUBLE | NOT NULL |  | Indicates whether the person has a hard-copy of contact list information on file with the institution |
| 24 | `CONTACT_METHOD_CD` | DOUBLE | NOT NULL |  | Denotes the person's preferred method of communication should he or she need to be contacted. |
| 25 | `CONTACT_TIME` | VARCHAR(255) |  |  | The preferred contact times and days for the person. |
| 26 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 27 | `CREDIT_HRS_TAKING` | DOUBLE |  |  | The current number of school credit hours the person is taking. |
| 28 | `CUMM_LEAVE_DAYS` | DOUBLE |  |  | future |
| 29 | `CURRENT_BALANCE` | DOUBLE |  |  | The current unpaid account balance owed by the person. |
| 30 | `CURRENT_GRADE` | DOUBLE |  |  | The current school grade of the person. |
| 31 | `CUSTODY_CD` | DOUBLE | NOT NULL |  | A person relationship code identifying the relationship of the person who has custody of the person. |
| 32 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 33 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 34 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 35 | `DEATH_CERTIFICATE_IDENT` | VARCHAR(100) |  |  | The numeric or textual identifier of the government issued vital document which certifies the patient's birth. |
| 36 | `DEGREE_COMPLETE_CD` | DOUBLE | NOT NULL |  | The highest degree completed by the person. |
| 37 | `DEMOG_VERIFY_DT_TM` | DATETIME |  |  | The date and time at which the patient's demographics were last verified. |
| 38 | `DIET_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies a special kind of diet for the person. |
| 39 | `DISEASE_ALERT_CD` | DOUBLE | NOT NULL |  | Identifies if the person has a disease that personnel need to be aware of. |
| 40 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 41 | `EXT_TRANSPORT_REQUIRED_CD` | DOUBLE | NOT NULL |  | Identifies if the patient requires transportation to the health care facility. |
| 42 | `FAMILY_INCOME` | DOUBLE |  |  | The current income of the person's immediate family. |
| 43 | `FAMILY_NBR_OF_MINORS_CNT` | DOUBLE |  |  | The current number of minors in the person's immediate family. |
| 44 | `FAMILY_SIZE` | DOUBLE |  |  | The current number of people in the person's immediate family. |
| 45 | `FINANCIAL_RISK_LEVEL_CD` | DOUBLE | NOT NULL |  | Indicates the person's propensity to make payment on bills for services rendered based on client-defined rules for evaluating financial risk level. |
| 46 | `FIN_STATEMENT_EXPIRE_DT_TM` | DATETIME |  |  | The date and time when the financial statement will expire for the person. |
| 47 | `FIN_STATEMENT_VERIFIED_DT_TM` | DATETIME |  |  | The date and time when the financial statement was verified for the person. |
| 48 | `GEST_AGE_AT_BIRTH` | DOUBLE |  |  | The gestational age at birth in days. |
| 49 | `GEST_AGE_METHOD_CD` | DOUBLE | NOT NULL |  | The code value for the method that was used to determine gestational age at birth. |
| 50 | `HEALTH_APP_ACCESS_OFFERED_CD` | DOUBLE | NOT NULL |  | the information regarding if the patient (or patient-authorized representative) has been offered access to any application(s) of their choosing made available by the provider which accesses their health information via a certified vendor API |
| 51 | `HEALTH_INFO_ACCESS_OFFERED_CD` | DOUBLE | NOT NULL |  | the information regarding if the patient (or patient-authorized representative) has been offered access to view online, download, and transmit their health information |
| 52 | `HIGHEST_GRADE_COMPLETE_CD` | DOUBLE | NOT NULL |  | The highest grade completed by the person. |
| 53 | `IMMUN_ON_FILE_CD` | DOUBLE | NOT NULL |  | future functionality |
| 54 | `INTERP_REQUIRED_CD` | DOUBLE | NOT NULL |  | Identifies that a language interpreter is required. Otherwise, this field is NULL. |
| 55 | `INTERP_TYPE_CD` | DOUBLE | NOT NULL |  | If the interp_required_cd is not null, then this field may be valued to indicate the need for a specific type of interpreter. |
| 56 | `IQH_PARTICIPANT_CD` | DOUBLE | NOT NULL |  | The IQ health participation code stores the consent status for IQ Health personal health record. |
| 57 | `LAST_ATD_ACTIVITY_DT_TM` | DATETIME |  |  | is this still used (V400)?? |
| 58 | `LAST_BILL_DT_TM` | DATETIME |  |  | The date and time that the last bill was sent to the person or insurance organization. |
| 59 | `LAST_BIND_DT_TM` | DATETIME |  |  | The last bind date and time of the patient |
| 60 | `LAST_DISCHARGE_DT_TM` | DATETIME |  |  | The date and time that the person was last discharged from the inpatient or ambulatory organization. |
| 61 | `LAST_EVENT_UPDT_DT_TM` | DATETIME |  |  | The date and time of the last clinical event of the patient. |
| 62 | `LAST_PAYMENT_DT_TM` | DATETIME |  |  | The date and time of the last payment received on behalf of the person. |
| 63 | `LAST_TRAUMA_DT_TM` | DATETIME |  |  | Date the last trauma related encounter occurred |
| 64 | `LIVING_ARRANGEMENT_CD` | DOUBLE | NOT NULL |  | The living arrangement of the patient |
| 65 | `LIVING_DEPENDENCY_CD` | DOUBLE | NOT NULL |  | The living dependency of the patient. |
| 66 | `LIVING_WILL_CD` | DOUBLE | NOT NULL |  | Provides a status of the patients living will. |
| 67 | `MICROFILM_CD` | DOUBLE | NOT NULL |  | Describes the existence of microfilm for the person's chart. |
| 68 | `MOTHER_IDENTIFIER` | VARCHAR(100) |  |  | Free-text attribute used to uniquely identify the persons mother |
| 69 | `MOTHER_IDENTIFIER_CD` | DOUBLE | NOT NULL |  | Identifies the type of alias specified in the MOTHER_IDENTIFIER attribute (MRN, SSN) |
| 70 | `NBR_OF_BROTHERS` | DOUBLE |  |  | The person's current number of brothers. |
| 71 | `NBR_OF_PREGNANCIES` | DOUBLE |  |  | Number of pregnancies |
| 72 | `NBR_OF_SISTERS` | DOUBLE |  |  | The person's current number of sisters. |
| 73 | `ORGAN_DONOR_CD` | DOUBLE | NOT NULL |  | Describes the organ donor status of the person. |
| 74 | `PARENT_MARITAL_STATUS_CD` | DOUBLE | NOT NULL |  | The marital status of the person's parents (I.e., divorced) |
| 75 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 76 | `PERSON_PATIENT_HIST_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person_patient_hist table. It is an internal system assigned number. |
| 77 | `PHONE_CONTACT_TYPE_CD` | DOUBLE | NOT NULL |  | Denotes the person's preferred type of phone should he or she need to be contacted. |
| 78 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 79 | `PREV_CONTACT_IND` | DOUBLE | NOT NULL |  | This attribute indicates if the patient has ever had previous contact with UK's NHS (National Health System). |
| 80 | `PRIMARY_CARE_HOME_CD` | DOUBLE | NOT NULL |  | Information regarding the patient's primary care home. A primary care home is a patient centered primary care setting where a group of medical professionals coordinate care within a defined population. |
| 81 | `PROCESS_ALERT_CD` | DOUBLE | NOT NULL |  | Identifies if there are special registration processes required for a person. |
| 82 | `SMOKES_CD` | DOUBLE | NOT NULL |  | Describes the smoking status of the person. |
| 83 | `SOURCE_LAST_SYNC_DT_TM` | DATETIME |  |  | The last date and time the record was synchronized with the master system. Added to support the UK's PDS serial change number. |
| 84 | `SOURCE_SYNC_LEVEL_FLAG` | DOUBLE | NOT NULL |  | Synchronization level indicates what level of synchronization with the master system is to be performed. 0 - the full person record should be synched with the master system when all other necessary criteria for synchronization have been met. 1 - the person record has been decoupled from the master system and no part of the record should be synched even when all other criteria necessary for synchronization have been met. |
| 85 | `SOURCE_VERSION_NUMBER` | VARCHAR(255) |  |  | Version number assigned from a master system to this record. added to support the uk's pds serial change number. |
| 86 | `STUDENT_CD` | DOUBLE | NOT NULL |  | Indicates if the patient is a student (full or part time). |
| 87 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history |
| 88 | `TRANSACTION_DT_TM` | DATETIME |  |  | More aptly named activity_dt_tm; holds the current date and time of the system when the row was inserted. This will match the create_dt_tm from the corresponding pm_hist_tracking row. |
| 89 | `TUMOR_REGISTRY_CD` | DOUBLE | NOT NULL |  | The tumor registry of the patient |
| 90 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 91 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 92 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 93 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 94 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 95 | `WRITTEN_FORMAT_CD` | DOUBLE | NOT NULL |  | This code indicates what is the preferred type of written communication that should be used for the patient. An example would be large print, braille, etc. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

