# STRT_MODEL_HL7_MAP

> Identifies which HL7 fields/components should be parsed for a given strt_model.

**Description:** Starter Model HL7 Map  
**Table type:** REFERENCE  
**Primary key:** `STRT_HL7_MAP_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMON_IND` | DOUBLE | NOT NULL |  | Indicates if this item should be saved and shared across result_sets. |
| 2 | `COMPONENT_CD` | DOUBLE | NOT NULL |  | Component code value |
| 3 | `COMPONENT_FORMAT_CD` | DOUBLE | NOT NULL |  | Identifies how a component should be formatted if required. |
| 4 | `COMPONENT_ORDER` | DOUBLE | NOT NULL |  | Order found in HL7 datastream |
| 5 | `COMPONENT_POSITION` | DOUBLE | NOT NULL |  | Identifies specific HL7 component within a field. |
| 6 | `FIELD_POSITION` | DOUBLE | NOT NULL |  | Identifies specific HL7 field within a segment. |
| 7 | `MAX_LENGTH` | DOUBLE | NOT NULL |  | Maximum number of characters expected for this field/component |
| 8 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates if this item is required in the result_set. 1 = yes, 0 = no. |
| 9 | `RESULT_SET_POSITION` | DOUBLE | NOT NULL |  | Defines the position in the result_set where this field/component should be stored. |
| 10 | `SEGMENT_CD` | DOUBLE | NOT NULL |  | Identifies HL7 segment |
| 11 | `STRT_HL7_MAP_ID` | DOUBLE | NOT NULL | PK | Sequence used as primary key |
| 12 | `STRT_MODEL_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | Identifies Starter Model format |
| 13 | `STRT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | This value is used to standardize Model information across systems. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `STRT_MODEL_FORMAT_ID` | [STRT_MODEL_FORMAT](STRT_MODEL_FORMAT.md) | `STRT_MODEL_FORMAT_ID` |
| `STRT_MODEL_ID` | [STRT_MODEL](STRT_MODEL.md) | `STRT_MODEL_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DEVICE_HL7_MAP](DEVICE_HL7_MAP.md) | `STRT_HL7_MAP_ID` |

