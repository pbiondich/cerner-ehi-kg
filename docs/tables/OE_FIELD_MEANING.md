# OE_FIELD_MEANING

> OE Field Meaning

**Description:** OE Field Meaning  
**Table type:** REFERENCE  
**Primary key:** `OE_FIELD_MEANING_ID`  
**Columns:** 8  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(200) |  |  | textual description |
| 2 | `OE_FIELD_MEANING` | VARCHAR(25) | NOT NULL |  | OE Field Meaning |
| 3 | `OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL | PK | OE Field Meaning Identifier. The value for this column does not come from an Oracle sequence. It is loaded via a CSV. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (8)

| From table | Column |
|------------|--------|
| [ORDER_DETAIL_HISTORY](ORDER_DETAIL_HISTORY.md) | `OE_FIELD_MEANING_ID` |
| [ORDER_PROPOSAL_DETAIL](ORDER_PROPOSAL_DETAIL.md) | `OE_FIELD_MEANING_ID` |
| [PM_PSO_LINK](PM_PSO_LINK.md) | `OE_FIELD_MEANING_ID` |
| [RX_MED_ORD_DETAIL](RX_MED_ORD_DETAIL.md) | `OE_FIELD_MEANING_ID` |
| [SCH_DETAIL](SCH_DETAIL.md) | `OE_FIELD_MEANING_ID` |
| [SCH_PEND_EVENT_DETAIL](SCH_PEND_EVENT_DETAIL.md) | `OE_FIELD_MEANING_ID` |
| [SCH_PEND_ORDER_DETAIL](SCH_PEND_ORDER_DETAIL.md) | `OE_FIELD_MEANING_ID` |
| [SCH_REF_DETAIL](SCH_REF_DETAIL.md) | `OE_FIELD_MEANING_ID` |

