# DD_SREF_CHF_CMPLNT_CRIT

> Each row on this table contains various criteria which should match when querying / looking up which structured documentation reference templates apply to a given patient and their current situation. This table provides the basis for flexing content intelligently.

**Description:** Dynamic Documentation - Structured Reference Chief Complaint Criteria  
**Table type:** REFERENCE  
**Primary key:** `DD_SREF_CHF_CMPLNT_CRIT_ID`  
**Columns:** 12  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHF_CMPLNT_IDENT` | VARCHAR(255) | NOT NULL |  | External identifier for this combination of criteria. |
| 2 | `CHF_CMPLNT_NAME` | VARCHAR(255) |  |  | Name to display when identifying the reason why a given template was matched / chosen for a given clinical scenario (patient, provider, setting). |
| 3 | `DD_SREF_CHF_CMPLNT_CRIT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a row on this table contains various criteria which should match when querying / looking up which structured documentation reference templates apply to a given patient and their current situation. This table provides the basis for flexing content intelligently. |
| 4 | `MAX_AGE_MONTHS` | DOUBLE | NOT NULL |  | The maximum age in months which this criteria is applicable for. The value not inclusive on the maximum side, allowing for contiguous ranges which will not return two rows for a specific aged patient. |
| 5 | `MIN_AGE_MONTHS` | DOUBLE | NOT NULL |  | The minimum age in months which this criteria is applicable for. The value is inclusive on the minimum side, so that if a patient's age is unknown, and is thus passed in as zero, this criteria should match. |
| 6 | `OCID_IDENT` | VARCHAR(255) | NOT NULL |  | DD_SREF_CHF_CMPLNT_CRIT may share the same OCID, but differ in their other parameters like age, sex, position and encounter type. This is a non-industry standard id to identify a group of criteria that share the same conceptual basis. |
| 7 | `SEX_CD` | DOUBLE | NOT NULL |  | The sex cd for which this criteria is applicable. A value of zero indicates that this criteria is not specific to any sex, and thus patients of any sex should match. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [DD_SDOC_SECT_TEMPL_RELTN](DD_SDOC_SECT_TEMPL_RELTN.md) | `DD_SREF_CHF_CMPLNT_CRIT_ID` |
| [DD_SREF_CRIT_ENC_TYP_RELTN](DD_SREF_CRIT_ENC_TYP_RELTN.md) | `DD_SREF_CHF_CMPLNT_CRIT_ID` |
| [DD_SREF_CRIT_POS_RELTN](DD_SREF_CRIT_POS_RELTN.md) | `DD_SREF_CHF_CMPLNT_CRIT_ID` |
| [DD_SREF_CRIT_TEMPL_RELTN](DD_SREF_CRIT_TEMPL_RELTN.md) | `DD_SREF_CHF_CMPLNT_CRIT_ID` |

