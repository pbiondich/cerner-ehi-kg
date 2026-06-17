# CONSENT_PROVISION

> Stores provisions for consents that contains an exception or additional information about the consent.

**Description:** Consent Provision  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONSENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the consent to which the provision is associated. |
| 4 | `CONSENT_PROVISION_ID` | DOUBLE | NOT NULL |  | The unique identifier of the Consent_Provision table. |
| 5 | `CONSENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | The flag indicating the type of the consent provision. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EXTERNAL_IDENT` | VARCHAR(36) |  |  | The unique identifier of the provision from an external system. |
| 8 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the organization associated with the provision. |
| 9 | `PROVISION_CATEGORY_FLAG` | DOUBLE | NOT NULL |  | Flag to represent the category for the provision created. |
| 10 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel identifier of the personnel associated with the provision. |
| 11 | `REASON_CD` | DOUBLE | NOT NULL |  | Code value indicating the reason the provision was created. |
| 12 | `REGISTRATION_RESULT_TXT` | VARCHAR(1000) |  |  | To store the free text returned by the foreign system |
| 13 | `REGISTRATION_STATUS_CD` | DOUBLE |  |  | Code value indicating the status of consent registered with external system |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONSENT_ID` | [CONSENT](CONSENT.md) | `CONSENT_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

