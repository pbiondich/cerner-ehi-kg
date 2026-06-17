# PERSON_FLEX_HIST

> Used for tracking history of certain columns on the person table.

**Description:** Person Flexible History Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 94

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABS_BIRTH_DT_TM` | DATETIME |  |  | The birth date/time "as entered" during registration. The date/time data in this field is "local" when the database is running in "UTC mode" and it is typically not populated (NULL) when the database is running in "local mode." This field is used for querying purposes only and helps eliminate edge cases where records fail to qualify because the user performing the search is in a different time zone than the patient. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `AGE_AT_DEATH` | DOUBLE | NOT NULL |  | The age of the person when they became deceased. |
| 7 | `AGE_AT_DEATH_PREC_MOD_FLAG` | DOUBLE | NOT NULL |  | Precision modifier used to represent the precision of the age of death. A flag of 0 means unknown. 1 - The age is less than the stated age of death. 2 - The age is greater than the stated age of death. 3 - The stated age of death is approximated. 4 - The stated age of death is exact. |
| 8 | `AGE_AT_DEATH_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measurement for the age at death. (Years, Months, Days or Hours) |
| 9 | `ARCHIVE_ENV_ID` | DOUBLE | NOT NULL |  | This column will indicate the environment_id that contains the data for this person. This column will be 0 for persons that have not been archived. |
| 10 | `ARCHIVE_STATUS_CD` | DOUBLE | NOT NULL |  | This column will indicate the archive status for this person. It will use a new code set that is not yet created. |
| 11 | `ARCHIVE_STATUS_DT_TM` | DATETIME |  |  | This column will indicate the last time this person was involved in an archive or restore. |
| 12 | `AUTOPSY_CD` | DOUBLE | NOT NULL |  | Indicates whether an autopsy has been performed on this person. |
| 13 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 14 | `BIRTH_DT_CD` | DOUBLE | NOT NULL |  | Birth date code indicates the kind of birth date and time value that is contained in the birth_dt_tm field. (i.e., estimated, still born, unknown, etc.) |
| 15 | `BIRTH_DT_TM` | DATETIME |  |  | The date and time of birth for the person. |
| 16 | `BIRTH_PREC_FLAG` | DOUBLE |  |  | Used to denote what information was captured for birth date and time. A flag of 0 means the date is precise to the day, a flag of 1 means the date is precise to the full date and time, a flag of 2 means the date is precise to month and a flag of 3 means the date is precise to year. |
| 17 | `BIRTH_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 18 | `CAUSE_OF_DEATH` | VARCHAR(100) |  |  | This is a text description of what caused the death of the person. |
| 19 | `CAUSE_OF_DEATH_CD` | DOUBLE | NOT NULL |  | This is a codified value of what caused the death of the person. |
| 20 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 21 | `CITIZENSHIP_CD` | DOUBLE | NOT NULL |  | Identifies the citizenship status for a person. |
| 22 | `CONCEPTION_DT_TM` | DATETIME |  |  | The date and time the person was conceived in the mother's womb. |
| 23 | `CONFID_LEVEL_CD` | DOUBLE | NOT NULL |  | Confidential level identifies a level of security that may restrict access or release of information. |
| 24 | `CONFID_LEVEL_SOURCE_CD` | DOUBLE |  |  | Defines the source that provided the confidentiality level information concerning a person. |
| 25 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 26 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the record was created. |
| 27 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The personnel ID of the person who created the row in the table. |
| 28 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 29 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 30 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 31 | `DECEASED_CD` | DOUBLE | NOT NULL |  | Identifies if the person is deceased. |
| 32 | `DECEASED_DT_TM` | DATETIME |  |  | The date and time of death for the person. |
| 33 | `DECEASED_DT_TM_PREC_FLAG` | DOUBLE | NOT NULL |  | Used to denote the precision of the deceased date and time. 0 - Precision is unknown. 1 - Date is precise to the full date and time. 2 - Date is precise to the month. 3 - Date is precise to the year. 4 - Date is precise to the day. |
| 34 | `DECEASED_ID_METHOD_CD` | DOUBLE | NOT NULL |  | Stores code values defining the specific way a patient was confirmed as being deceased. Possible values include Death Certificate, Physician Reported, etc. The code values are closely tied, workflow-wise, to the Deceased_Source_Cd which records if a patient was identified as being deceased from a Formal (Death Certificate) or Informal (no Death Certificate) source and the Deceased_Notify_Source_Cd which records who\ what provided the information regarding the patient's deceased status. |
| 35 | `DECEASED_NOTIFY_SOURCE_CD` | DOUBLE |  |  | Defines the particular source that gave notification regarding the deceased information concerning a person. For example, from a Government Agency Record, Inpatient Death, or Other. |
| 36 | `DECEASED_SOURCE_CD` | DOUBLE | NOT NULL |  | Defines the particular source that deceased information concerning a person was given. |
| 37 | `DECEASED_TZ` | DOUBLE | NOT NULL |  | The time zone where the deceased date was entered. |
| 38 | `EMANCIPATION_DT_TM` | DATETIME |  |  | The date and time when the person was emancipated. |
| 39 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 40 | `ETHNIC_GRP_CD` | DOUBLE | NOT NULL |  | Identifies a religious, national, racial, or cultural group of the person. |
| 41 | `FT_ENTITY_ID` | DOUBLE | NOT NULL |  | Used to identify the ID of the free textentity which this free textperson row is associated with. |
| 42 | `FT_ENTITY_NAME` | VARCHAR(32) |  |  | Name of the entity for which this free textperson row is associated. |
| 43 | `LANGUAGE_CD` | DOUBLE | NOT NULL |  | The primary language spoken by the person. |
| 44 | `LANGUAGE_DIALECT_CD` | DOUBLE | NOT NULL |  | The dialect of the primary language spoken by the person. |
| 45 | `LAST_ACCESSED_DT_TM` | DATETIME | NOT NULL |  | This column contains the date/time this person was last accessed. It affects when the person will be archived when archiving is active. |
| 46 | `LAST_ENCNTR_DT_TM` | DATETIME |  |  | The date and time of the last encounter for the person. |
| 47 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 48 | `MARITAL_TYPE_CD` | DOUBLE | NOT NULL |  | This field identifies the status of the person with regard to being married. |
| 49 | `MILITARY_BASE_LOCATION` | VARCHAR(100) |  |  | The location of the military base at which the person is stationed. |
| 50 | `MILITARY_RANK_CD` | DOUBLE | NOT NULL |  | Military ranking of individual (i.e. Private, Seargent, General, etc.) |
| 51 | `MILITARY_SERVICE_CD` | DOUBLE | NOT NULL |  | Military status of an individual (i.e. Active Duty, Reserves, etc.) |
| 52 | `MOTHER_MAIDEN_NAME` | VARCHAR(100) |  |  | The mother's last name she was given at birth. |
| 53 | `NAME_FIRST` | VARCHAR(200) |  |  | This is the person's given first name. |
| 54 | `NAME_FIRST_KEY` | VARCHAR(100) |  |  | This is the person's first given name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 55 | `NAME_FIRST_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_FIRST_KEY_A_NLS column |
| 56 | `NAME_FIRST_KEY_NLS` | VARCHAR(202) |  |  | First Name Key field converted to NLS format for internationalization requirements |
| 57 | `NAME_FIRST_PHONETIC` | VARCHAR(8) |  |  | Phonetic representation of person's first name. |
| 58 | `NAME_FIRST_SYNONYM_ID` | DOUBLE | NOT NULL |  | First Name Synonym Id |
| 59 | `NAME_FULL_FORMATTED` | VARCHAR(100) |  |  | This is the complete person name including punctuation and formatting. |
| 60 | `NAME_LAST` | VARCHAR(200) |  |  | This is the person's family name. |
| 61 | `NAME_LAST_KEY` | VARCHAR(100) |  |  | This is the person's family name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 62 | `NAME_LAST_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_LAST_KEY_A_NLS column |
| 63 | `NAME_LAST_KEY_NLS` | VARCHAR(202) |  |  | Last Name Key field converted to NLS format for internationalization requirements |
| 64 | `NAME_LAST_PHONETIC` | VARCHAR(8) |  |  | Phonetic representation of person's last name. |
| 65 | `NAME_MIDDLE` | VARCHAR(200) |  |  | This is the given middle name for the person. |
| 66 | `NAME_MIDDLE_KEY` | VARCHAR(100) |  |  | This is the person's middle name with all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 67 | `NAME_MIDDLE_KEY_A_NLS` | VARCHAR(400) |  |  | NAME_MIDDLE_KEY_A_NLS column |
| 68 | `NAME_MIDDLE_KEY_NLS` | VARCHAR(202) |  |  | Last Name Key field converted to NLS format for internationalization requirements |
| 69 | `NAME_PHONETIC` | CHAR(8) |  |  | This is the Soundex coded representation of the person's name. This field is used for indexing and searching for a patient by name when the exact spelling is not known. |
| 70 | `NATIONALITY_CD` | DOUBLE | NOT NULL |  | This field Identifies the nationality associated with the person. |
| 71 | `NEXT_RESTORE_DT_TM` | DATETIME |  |  | This column contains the date/time when this person needs to be restored from archive. |
| 72 | `PERSONAL_PRONOUN_CD` | DOUBLE |  |  | The person's desired personal pronouns to use as a simple substitue for their proper name that they feel best represents their gender identity. Examples may include She/Her/Hers, He/Him/His,They/Them/Theirs, etc. |
| 73 | `PERSONAL_PRONOUN_OTHER_TXT` | VARCHAR(100) |  |  | The other personal pronoun text of the person when the person's personal pronoun code is OTHER. |
| 74 | `PERSON_FLEX_HIST_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person_flex_hist table. It is an internal system assigned number. |
| 75 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 76 | `PERSON_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the person |
| 77 | `PERSON_TYPE_CD` | DOUBLE | NOT NULL |  | The person type field identifies the general type of data being stored in a given person row. As a general guideline, most rows in the person table will be identified with a person type of PERSON. This field can be used to filter out NON-PERSON rows. |
| 78 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 79 | `PURGE_OPTION_CD` | DOUBLE | NOT NULL |  | OBSOLETE: Purge Option Code Value |
| 80 | `RACE_CD` | DOUBLE | NOT NULL |  | A group of people classified together on the basis of common history, nationality, or geographical distribution. |
| 81 | `RELIGION_CD` | DOUBLE | NOT NULL |  | A particular integrated system of belief in a supernatural power. |
| 82 | `RESIDENT_CD` | DOUBLE | NOT NULL |  | Identifies the resident status for a person. |
| 83 | `SEX_AGE_CHANGE_IND` | DOUBLE |  |  | This field indicates that the sex of the person has changed as the result of a correction of the data or actual physical change to the person. |
| 84 | `SEX_CD` | DOUBLE | NOT NULL |  | The sex/gender that the patient is considered to have for administration and record keeping purposes. This is typically asserted by the patient when they present to administrative users. This may not match the biological sex as determined by anatomy or genetics, or the individual's preferred identification (gender identity). |
| 85 | `SPECIES_CD` | DOUBLE | NOT NULL |  | A fundamental category of taxonomic classification, ranking after a genus and consisting of organisms capable of interbreeding. |
| 86 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 87 | `TRANSACTION_DT_TM` | DATETIME |  |  | More aptly named activity_dt_tm; holds the current date and time of the system when the row was inserted. This will match the create_dt_tm from the corresponding pm_hist_tracking row. |
| 88 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 89 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 90 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 91 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 92 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 93 | `VET_MILITARY_STATUS_CD` | DOUBLE | NOT NULL |  | Identifies the military status of a service veteran. |
| 94 | `VIP_CD` | DOUBLE | NOT NULL |  | Identifies and used to communicate that the person is identified as deserving special consideration during the stay or visit. A security level (confid_level_cd) may or may not be implied by a V.I.P. code. Examples include employee, famous person, etc. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

