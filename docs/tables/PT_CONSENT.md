# PT_CONSENT

> This table stores the information related to consents.

**Description:** PT CONSENT  
**Table type:** ACTIVITY  
**Primary key:** `PT_CONSENT_ID`  
**Columns:** 25  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CONSENTING_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the organization table. This field identifies the institution with which the person consenting the patient was affiliated. For this purpose, an institution can be another hospital, research institute, drug company, government agency, etc. |
| 3 | `CONSENTING_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the person table. This field identifies the individual who consented the patient. |
| 4 | `CONSENT_ID` | DOUBLE | NOT NULL |  | Logical identifier into the pt_consent table. No two active rows (End_effective_dt_tm = 31-dec-2100) will have the same consent_id |
| 5 | `CONSENT_NBR` | DOUBLE | NOT NULL |  | This filed is a sequence number of consent released for a person on a protocol. |
| 6 | `CONSENT_RECEIVED_DT_TM` | DATETIME |  |  | Date and time on which the consent was received |
| 7 | `CONSENT_RECEIVED_TM_IND` | DOUBLE | NOT NULL |  | This column identifies whether time is entered by user from front end for Consent Received Time field |
| 8 | `CONSENT_RELEASED_DT_TM` | DATETIME |  |  | Date and time at which the consent was released |
| 9 | `CONSENT_RELEASED_TM_IND` | DOUBLE | NOT NULL |  | This column identifies whether time is entered by user from front end for Consent Released Time field |
| 10 | `CONSENT_SIGNED_DT_TM` | DATETIME | NOT NULL |  | Date and time at which the consent was signed |
| 11 | `CONSENT_SIGNED_TM_IND` | DOUBLE | NOT NULL |  | This column identifies whether time is entered by user from front end for Consent Signed Time field |
| 12 | `CT_DOCUMENT_VERSION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the consent document associated with the patient and the protocol |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `NOT_RETURNED_DT_TM` | DATETIME | NOT NULL |  | The date and time on which it is determined that consent will not be returned |
| 15 | `NOT_RETURNED_REASON_CD` | DOUBLE | NOT NULL |  | The reason why consent was not returned |
| 16 | `NOT_RETURNED_TM_IND` | DOUBLE | NOT NULL |  | This column identifies whether time is entered by user from front end for Not Returned Time field |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 18 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the amendment for which the consent belongs |
| 19 | `PT_CONSENT_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the pt_consent table. It is an internal system assigned number. |
| 20 | `REASON_FOR_CONSENT_CD` | DOUBLE | NOT NULL |  | This field contains a code identifying the reason the patient was consented for this protocol enrollment. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONSENTING_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `CONSENTING_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `CT_DOCUMENT_VERSION_ID` | [CT_DOCUMENT_VERSION](CT_DOCUMENT_VERSION.md) | `CT_DOCUMENT_VERSION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CT_REASON_DELETED](CT_REASON_DELETED.md) | `CONSENT_ID` |
| [PT_ELIG_CONSENT_RELTN](PT_ELIG_CONSENT_RELTN.md) | `CONSENT_ID` |
| [PT_REG_CONSENT_RELTN](PT_REG_CONSENT_RELTN.md) | `CONSENT_ID` |

