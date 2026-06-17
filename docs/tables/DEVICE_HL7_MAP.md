# DEVICE_HL7_MAP

> Identifies which HL7 fields/components should be parsed for a given device.

**Description:** Device HL7 Map  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMMON_IND` | DOUBLE | NOT NULL |  | Indicates if this item should be saved and shared across result_sets.Column |
| 3 | `COMPONENT_CD` | DOUBLE | NOT NULL |  | Component code value |
| 4 | `COMPONENT_FORMAT_CD` | DOUBLE | NOT NULL |  | Identifies how a component should be formatted if required. |
| 5 | `COMPONENT_ORDER` | DOUBLE | NOT NULL |  | Order found in HL7 Data stream |
| 6 | `COMPONENT_POSITION` | DOUBLE | NOT NULL |  | Identifies specific HL7 component within a field. |
| 7 | `DEVICE_CD` | DOUBLE | NOT NULL | FK→ | Used to provide Device HL7 Map across service resources. |
| 8 | `DEVICE_HL7_MAP_ID` | DOUBLE | NOT NULL |  | Sequence used as primary key. |
| 9 | `FIELD_POSITION` | DOUBLE | NOT NULL |  | Identifies specific HL7 field within a segment. |
| 10 | `MAX_LENGTH` | DOUBLE | NOT NULL |  | Maximum number of characters expected for this field/component |
| 11 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates if this item is required in the result_set. 1 = yes, 0 = no. |
| 12 | `RESULT_SET_POSITION` | DOUBLE | NOT NULL |  | Defines the position in the result_set where this field/component should be stored. |
| 13 | `SEGMENT_CD` | DOUBLE | NOT NULL |  | Identifies HL7 segment |
| 14 | `STRT_HL7_MAP_ID` | DOUBLE | NOT NULL | FK→ | Identifies HL7 Map format |
| 15 | `STRT_MODEL_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Start Model Format. FK from STRT_MODEL_FORMAT |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEVICE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `STRT_HL7_MAP_ID` | [STRT_MODEL_HL7_MAP](STRT_MODEL_HL7_MAP.md) | `STRT_HL7_MAP_ID` |
| `STRT_MODEL_FORMAT_ID` | [STRT_MODEL_FORMAT](STRT_MODEL_FORMAT.md) | `STRT_MODEL_FORMAT_ID` |

