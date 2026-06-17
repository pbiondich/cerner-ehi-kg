# CT_PROT_AMD_CUSTOM_FLD_VAL

> This table stores the values entered for a custom field.

**Description:** Protocol amendment custom field value  
**Table type:** REFERENCE  
**Primary key:** `CT_PROT_AMD_CUSTOM_FLD_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CT_CUSTOM_FIELD_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the ct_custom_field table. |
| 3 | `CT_PROT_AMD_CUSTOM_FLD_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FIELD_POSITION` | DOUBLE | NOT NULL |  | A number which identifies the positon of the field |
| 6 | `PREV_CT_PROT_AMD_CUSTOM_FLD_ID` | DOUBLE | NOT NULL | FK→ | The original value of the ct_prot_amd_custom_field_value_id used for grouping the related versons. Required for type 2 versioning methodology. |
| 7 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | This field uniquely identifies a row in the prot_amendment table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALUE_CD` | DOUBLE | NOT NULL |  | This field contains the code that was selected by the user. The code set from which it is from is defined by the ct_custom_field_id record.Flex on code sets. |
| 14 | `VALUE_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time entered in by the user. |
| 15 | `VALUE_TEXT` | VARCHAR(255) | NOT NULL |  | This field contains the text entered in by the user. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CT_CUSTOM_FIELD_ID` | [CT_CUSTOM_FIELD](CT_CUSTOM_FIELD.md) | `CT_CUSTOM_FIELD_ID` |
| `PREV_CT_PROT_AMD_CUSTOM_FLD_ID` | [CT_PROT_AMD_CUSTOM_FLD_VAL](CT_PROT_AMD_CUSTOM_FLD_VAL.md) | `CT_PROT_AMD_CUSTOM_FLD_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CT_PROT_AMD_CUSTOM_FLD_VAL](CT_PROT_AMD_CUSTOM_FLD_VAL.md) | `PREV_CT_PROT_AMD_CUSTOM_FLD_ID` |

