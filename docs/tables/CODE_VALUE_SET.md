# CODE_VALUE_SET

> Used to store the list of code_sets and their descriptions as well as other attributes about a code_set.

**Description:** Used to store the list of code_sets.  
**Table type:** REFERENCE  
**Primary key:** `CODE_SET`  
**Columns:** 30  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND_DUP_IND` | DOUBLE |  |  | Indicates whether the ACTIVE_IND field is being used for duplicate checking when adding/updating code values. |
| 2 | `ADD_ACCESS_IND` | DOUBLE |  |  | Indicates whether the user may add code values to this code set. |
| 3 | `ALIAS_DUP_IND` | DOUBLE |  |  | The alias, alias_type_meaning, code_set, and contributor_system_cd on the code_value_alias table will be used for duplicate checking. |
| 4 | `CACHE_IND` | DOUBLE |  |  | Indicates whether this code set will be cached by the decoder |
| 5 | `CDF_MEANING_DUP_IND` | DOUBLE |  |  | Indicates whether the CDF Meaning field on the code value table will be used for duplicate checking when adding/updating code values. |
| 6 | `CHG_ACCESS_IND` | DOUBLE |  |  | Indicates whether the user can change code values in CRMCode. |
| 7 | `CODE_SET` | DOUBLE | NOT NULL | PK | The number of the code set header record (determined by following the procedure for creating a new code set). |
| 8 | `CODE_SET_HITS` | DOUBLE |  |  | Used by the decoders. |
| 9 | `CODE_VALUES_CNT` | DOUBLE |  |  | Used by the decoders. |
| 10 | `CONTRIBUTOR` | VARCHAR(18) |  |  | Obsolete |
| 11 | `DEFINITION` | VARCHAR(500) |  |  | Definition. |
| 12 | `DEFINITION_DUP_IND` | DOUBLE |  |  | definition duplicate indicator |
| 13 | `DEF_DUP_RULE_FLAG` | DOUBLE |  |  | Defines how the code set should be handled during merge. |
| 14 | `DEL_ACCESS_IND` | DOUBLE |  |  | Controls whether code values can be deleted in CRMCODE |
| 15 | `DESCRIPTION` | VARCHAR(60) |  |  | description of the code set |
| 16 | `DISPLAY` | VARCHAR(40) |  |  | display of the code set |
| 17 | `DISPLAY_DUP_IND` | DOUBLE |  |  | Indicates whether DISPLAY field on the code value table will be used for duplicate checking when inserting/updating code values. |
| 18 | `DISPLAY_KEY` | VARCHAR(40) |  |  | Similar to DISPLAY but contains only upper case and alphanumeric characters without any special characters or embedded spaces; Typically used in index to improve query performanced |
| 19 | `DISPLAY_KEY_DUP_IND` | DOUBLE |  |  | use display_key as the duplicate check for this code set |
| 20 | `DOMAIN_CODE_SET` | DOUBLE |  |  | Not used. |
| 21 | `DOMAIN_QUALIFIER_IND` | DOUBLE |  |  | not used |
| 22 | `EXTENSION_IND` | DOUBLE |  |  | Indicates whether code_set_extension rows exist |
| 23 | `INQ_ACCESS_IND` | DOUBLE |  |  | determines whether this code set can be viewed in crmcode |
| 24 | `OWNER_MODULE` | VARCHAR(12) |  |  | Not used. |
| 25 | `TABLE_NAME` | VARCHAR(32) |  |  | Not used. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (9)

| From table | Column |
|------------|--------|
| [CODE_DOMAIN_FILTER](CODE_DOMAIN_FILTER.md) | `CODE_SET` |
| [CODE_SET_EXTENSION](CODE_SET_EXTENSION.md) | `CODE_SET` |
| [CODE_SET_FIELD_DOMAIN](CODE_SET_FIELD_DOMAIN.md) | `CODE_SET` |
| [CODE_SET_INTERFACE](CODE_SET_INTERFACE.md) | `CODE_SET` |
| [CODE_VALUE_ALIAS](CODE_VALUE_ALIAS.md) | `CODE_SET` |
| [CODE_VALUE_OUTBOUND](CODE_VALUE_OUTBOUND.md) | `CODE_SET` |
| [COMMON_DATA_FOUNDATION](COMMON_DATA_FOUNDATION.md) | `CODE_SET` |
| [REGIMEN_CAT_ATTRIBUTE](REGIMEN_CAT_ATTRIBUTE.md) | `CODE_SET` |
| [SCH_CODE_REF](SCH_CODE_REF.md) | `CODE_SET` |

