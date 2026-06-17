# CONSENT

> Contains patient data consents

**Description:** Consent  
**Table type:** ACTIVITY  
**Primary key:** `CONSENT_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONSENT_CATEGORY_FLAG` | DOUBLE | NOT NULL |  | Flag indicating the category of the consent |
| 4 | `CONSENT_GIVEN_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person identifier of the person acting on behalf of the patient. |
| 5 | `CONSENT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the consent table. |
| 6 | `CONSENT_LEVEL_FLAG` | DOUBLE | NOT NULL |  | Flag indicating the level of the consent |
| 7 | `CONSENT_SCOPE_FLAG` | DOUBLE | NOT NULL |  | Flag indicating the scope of the consent |
| 8 | `CONSENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag indicating the type of the consent. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EXTERNAL_IDENT` | VARCHAR(36) |  |  | Unique identifier of the consent in external systems |
| 11 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the organization associated with the consent. |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the patient to which the consent applies . |
| 13 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel identifier of the personnel associated with the consent. |
| 14 | `REASON_CD` | DOUBLE | NOT NULL |  | Code Value indicating the reason the consent was created.; |
| 15 | `REGISTRATION_RESULT_TXT` | VARCHAR(1000) |  |  | To store the free text returned by the foreign system |
| 16 | `REGISTRATION_STATUS_CD` | DOUBLE |  |  | Code value indicating the status of consent registered with external system; |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONSENT_GIVEN_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CONSENT_PROVISION](CONSENT_PROVISION.md) | `CONSENT_ID` |

