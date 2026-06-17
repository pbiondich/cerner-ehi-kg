# IMMUNIZATION_MODIFIER

> This is the list of modifiers to expectations and Immunization events.

**Description:** IMMUNIZATION MODIFIER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CLINICAL_EVENT_ID` | DOUBLE | NOT NULL |  | THIS COLUMN NOT USED. Clinical event identifier (from CLINICAL_EVENT) related to this modifier information. This column is not used and will be made obsolete. Use EVENT_ID instead. 6/25/03 |
| 3 | `CONSENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | OBSOLETE - ID to LONG_TEXT for comments related to the consent for the related Expectation. |
| 4 | `CONSENT_PERSON_ID` | DOUBLE | NOT NULL | FK→ | OBSOLETE - ID from PERSON of the person giving consent for the Expectation. |
| 5 | `CONSENT_PERSON_REL_CD` | DOUBLE | NOT NULL |  | OBSOLETE - Value from CS40 to indicate the relationship of the person giving consent for the person identified by person_id. |
| 6 | `DEFAULT_EVENT_IND` | DOUBLE |  |  | Indicates whether the event for the immunization was selected by default. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EVENT_CD` | DOUBLE | NOT NULL |  | The event code that corresponds to this modifier. |
| 9 | `EVENT_ID` | DOUBLE | NOT NULL |  | This value comes from the non-key EVENT_ID column in the CLINICAL_EVENT table. |
| 10 | `EXPECT_MEANING` | VARCHAR(250) | NOT NULL |  | The Expectation meaning of the HM Expectation associated with the modifier. |
| 11 | `FUNDING_SOURCE_CD` | DOUBLE | NOT NULL |  | The funding source code associated to this modifier. |
| 12 | `IMMUNIZATION_MODIFIER_ID` | DOUBLE | NOT NULL |  | Unique Identifier for the immunization_modifier table. |
| 13 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key from ORGANIZATION table |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `VFC_STATUS_CD` | DOUBLE | NOT NULL |  | The Code that identifies the Vaccines For Children (VFC) status for the related Expectation. |
| 21 | `VIS_CD` | DOUBLE | NOT NULL |  | The Vaccine Information Statement code associated to this modifier |
| 22 | `VIS_DT_ISO` | VARCHAR(10) |  |  | Stores a string value of the Vaccine Information Statement (VIS) published on date in the following ISO supported formats:; YYYYMMDD |
| 23 | `VIS_DT_TM` | DATETIME |  |  | The version date printed on the Vaccine Information Sheet (VIS) for the related Expectation. |
| 24 | `VIS_GIVEN_ON_DT_ISO` | VARCHAR(10) |  |  | Stores a string value of the Vaccine Information Statement (VIS) given on date in the following ISO supported format:; YYYYMMDD |
| 25 | `VIS_PROVIDED_ON_DT_TM` | DATETIME |  |  | The date and time that the VIS was provided to the patient or their parent/guardian |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONSENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `CONSENT_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

