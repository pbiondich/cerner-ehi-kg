# ORDER_ENTRY_FIELDS

> The table containing all the fields that may be used to capture information about an order.

**Description:** ORDER ENTRY FIELDS  
**Table type:** REFERENCE  
**Primary key:** `OE_FIELD_ID`  
**Columns:** 34  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_SIZE` | DOUBLE |  |  | The size of the field. |
| 2 | `ALLOW_MULTIPLE_IND` | DOUBLE |  |  | An indicator on whether the field can appear multiple times on a format. |
| 3 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | The catalog type this field may be associated with, optional. |
| 4 | `CKI` | VARCHAR(30) |  |  | Cerner Knowledge Index for this order entry field |
| 5 | `CODESET` | DOUBLE |  |  | If the field is verified against a codeset, this is the codeset to use. |
| 6 | `COMMON_FLAG` | DOUBLE |  |  | Flag on whether or not to show the field in common order details. |
| 7 | `DESCRIPTION` | VARCHAR(100) |  |  | The description of the field |
| 8 | `EVENT_CD` | DOUBLE | NOT NULL |  | If 'smart defaulting' is being used, the event code for the last result to retrieve as a default. |
| 9 | `FIELD_TYPE_FLAG` | DOUBLE |  |  | Flag used to identify the type of field it it. |
| 10 | `FSI_MAP_TO_OBX_IND` | DOUBLE |  |  | Indicates that this order_entry_field should be considered for outbound interface |
| 11 | `HELP_CONTEXT_ID` | DOUBLE | NOT NULL |  | Future. |
| 12 | `HIDE_FEMALE_IND` | DOUBLE |  |  | Indicates whether this field should be hidden for female patients. |
| 13 | `HIDE_MALE_IND` | DOUBLE |  |  | Indicates whether this field should be hidden for male patients. |
| 14 | `HIDE_MAX_AGE` | DOUBLE |  |  | The age to be older than to hide this field. |
| 15 | `HIDE_MAX_AGE_IND` | DOUBLE |  |  | whether this field should be hidden for patients older than a specified age. |
| 16 | `HIDE_MAX_AGE_UNITS_FLAG` | DOUBLE |  |  | The unit type for the max age. |
| 17 | `HIDE_MIN_AGE` | DOUBLE |  |  | The age to be younger than to hide this field. |
| 18 | `HIDE_MIN_AGE_IND` | DOUBLE |  |  | Indicates whether this field should be hidden for patients under a specified age. |
| 19 | `HIDE_MIN_AGE_UNITS_FLAG` | DOUBLE |  |  | The unit type for the minimum age. |
| 20 | `MAX_VAL` | DOUBLE |  |  | The maximum value possible for a field if it is a numeric type. |
| 21 | `MIN_VAL` | DOUBLE |  |  | The minimum value of the field if it is a numeric type. |
| 22 | `OE_FIELD_ID` | DOUBLE | NOT NULL | PK | The id of the order entry field. |
| 23 | `OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL |  | The Cerner defined id that identifies what the field is being used for. |
| 24 | `PROMPT_ENTITY_ID` | DOUBLE | NOT NULL |  | The identifier for the prompt test that is located on another table. This could be a task_assay_cd. |
| 25 | `PROMPT_ENTITY_NAME` | VARCHAR(32) |  |  | The table name where the prompt test field is located, for example DISCRETE_TASK_ASSAY. This field is empty for non-prompt fields. |
| 26 | `REQUEST` | DOUBLE |  |  | Future |
| 27 | `SMART_DEFAULTING_FLAG` | DOUBLE |  |  | Flag to identify the type of defaulting this field - update or non-update ocf. |
| 28 | `SPIN_INCREMENT_CNT` | DOUBLE |  |  | For a numeric field the amount a spin control should increment by. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `VALIDATION_TYPE_FLAG` | DOUBLE |  |  | The type of validation to verify the field. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (9)

| From table | Column |
|------------|--------|
| [AP_PROMPT_FIELD](AP_PROMPT_FIELD.md) | `OE_FIELD_ID` |
| [ORDER_DETAIL_HISTORY](ORDER_DETAIL_HISTORY.md) | `OE_FIELD_ID` |
| [ORDER_PROPOSAL_DETAIL](ORDER_PROPOSAL_DETAIL.md) | `OE_FIELD_ID` |
| [ORDER_SENTENCE_DETAIL](ORDER_SENTENCE_DETAIL.md) | `OE_FIELD_ID` |
| [SCH_DETAIL](SCH_DETAIL.md) | `OE_FIELD_ID` |
| [SCH_FLEX_LIST](SCH_FLEX_LIST.md) | `OE_FIELD_ID` |
| [SCH_PEND_EVENT_DETAIL](SCH_PEND_EVENT_DETAIL.md) | `OE_FIELD_ID` |
| [SCH_PEND_ORDER_DETAIL](SCH_PEND_ORDER_DETAIL.md) | `OE_FIELD_ID` |
| [SCH_REF_DETAIL](SCH_REF_DETAIL.md) | `OE_FIELD_ID` |

