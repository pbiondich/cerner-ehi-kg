# PL_CLIENT_DEFAULTS

> This table stores client level default settings.

**Description:** PL CLIENT DEFAULTS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 41

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_COPIES` | DOUBLE |  |  | Notifies Pahtlink Applications of how many ABN forms to print. |
| 2 | `BILL_TYPE_FLAG` | DOUBLE |  |  | Determines the need for bill type in ePathLink Applications. |
| 3 | `BILL_TYPE_IND` | DOUBLE |  |  | Indicates whether client or patient bill type will be selected by default |
| 4 | `CLIENT_BILL_ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | This represents the encounter type that is used when client bill type is chosen. |
| 5 | `CLIENT_BILL_FIN_CLASS_CD` | DOUBLE | NOT NULL |  | The financial class to be used when client bill type is selected. |
| 6 | `CLIENT_SEQUENCE` | DOUBLE |  |  | Used to determine if a default row exists. |
| 7 | `COLLECTION_PRIORITY_CD` | DOUBLE | NOT NULL |  | This determines the default COLLECT PRIORITY. |
| 8 | `COLLECT_BY_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Indicates the default person id to appear in the Collected By field. |
| 9 | `COLLECT_BY_USER_IND` | DOUBLE |  |  | Indicates whether or not to default the current user's user ID into the Collected By field. |
| 10 | `CREATE_MRN_IND` | DOUBLE |  |  | Indicates a new MRN should be created if one has not already been created. |
| 11 | `CURDATE_IND` | DOUBLE |  |  | Indicates whether or not to default the current date into the collection date field |
| 12 | `CURTIME_IND` | DOUBLE |  |  | Indicates whether or not to default the current time into the collection time field. |
| 13 | `DIAGNOSIS_FLAG` | DOUBLE |  |  | Indicates whether order level diagnosis are required based on bill type. |
| 14 | `FINANCIAL_CLASS_LABEL` | VARCHAR(30) |  |  | User-defined label for the data field receiving financial class. |
| 15 | `FIN_ASSIGNMENT_FLAG` | DOUBLE |  |  | Indicates how the financial number is assigned |
| 16 | `FIN_BY_PLAN_FLAG` | DOUBLE |  |  | Indicate3s whether or not to default the financial class based on the selected primary insurance health plan (0 - Do not default, 1 - Default if client bill, 2 - Default if patient bill, or 3 - Default). |
| 17 | `FIN_CLASS_FLAG` | DOUBLE |  |  | Indicates when the field should be enabled, required, or disabled. |
| 18 | `INSURANCE_CO_FLAG` | DOUBLE |  |  | Indicates whether or not the insurance company field on the insurance tab in ePathlink should be required, enabled but not required, or disabled based on bill type. |
| 19 | `LOCATION_FLAG` | DOUBLE |  |  | Determines whether or not buildings or ambulatory locations are used to populate the location list in the app. |
| 20 | `MRN_ASSIGNMENT_FLAG` | DOUBLE |  |  | Indicates how the medical record number should get assigned |
| 21 | `NEW_REG_FLAG` | DOUBLE |  |  | Indicates how the person and encounter is selected or created during and ordering conversation. |
| 22 | `ORDERING_PHYS_DISPLAY` | VARCHAR(30) |  |  | Indicates the default ordering physician |
| 23 | `ORDERING_PHYS_ID` | DOUBLE | NOT NULL |  | Indicates the default ordering physician's ID |
| 24 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization id is the key to the table, which identifies the client for which these defaults will be used. |
| 25 | `ORG_SECURITY_IND` | DOUBLE |  |  | Indicates whether organization level security is turned on if Lab organization security is off. |
| 26 | `PATIENT_ALIAS_FLAG` | DOUBLE |  |  | Indicates whether or not this field is required or disabled. |
| 27 | `PATIENT_BILL_ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the encounter type to use when patient bill type is selected. |
| 28 | `PATIENT_BILL_FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Indicates the financial class to use when patient bill type is selected. |
| 29 | `PERSON_SECURITY_IND` | DOUBLE |  |  | Indicates whether person level security is turned on or not. |
| 30 | `PHONE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the default call back phone type |
| 31 | `REG_PHYSICIAN_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the physician type to be used for the registering physicians. |
| 32 | `REG_PHYS_TYPE_DISPLAY` | VARCHAR(30) |  |  | Indicates the label to be used above the registering physician selection field. |
| 33 | `REPORTING_PRIORITY_CD` | DOUBLE | NOT NULL |  | Indicates the default reporting priority to be used |
| 34 | `REQUIRED_DIAGNOSIS_FLAG` | DOUBLE |  |  | Indicates whether or not an encounter level diagnosis is required based on the selected bill type. |
| 35 | `SEARCH_START_FLAG` | DOUBLE |  |  | Detremines the need for this field in PathLink Applications. |
| 36 | `TRIGGER_ADT_IND` | DOUBLE |  |  | Indicates whether or not person/encounter updates will trigger an ADT. |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 40 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 41 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COLLECT_BY_PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

