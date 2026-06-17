# RX_METHOD_RELTN

> One of the calculation types, (Adjusted Body Weight) is dependent on having an Ideal Body Weight. This will let the user specify Ideal Body Weight method they want to use for this calculation.

**Description:** PharmNet Method Relation  
**Table type:** REFERENCE  
**Primary key:** `RX_METHOD_RELTN_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CHILD_METHOD_ID` | DOUBLE | NOT NULL | FK→ | User selected method of performing some formula. If this field contains a zero, the system selected the method. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `PARENT_METHOD_ID` | DOUBLE | NOT NULL | FK→ | A method that can have multiple choices for implementation. Example Adjusted Body Weight. |
| 6 | `RX_METHOD_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RX_METHOD_RELTN table. |
| 7 | `RX_METHOD_RELTN_P_ID` | DOUBLE | NOT NULL | FK→ | Used for grouping versions of a method relation. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_METHOD_ID` | [RX_METHOD](RX_METHOD.md) | `RX_METHOD_ID` |
| `PARENT_METHOD_ID` | [RX_METHOD](RX_METHOD.md) | `RX_METHOD_ID` |
| `RX_METHOD_RELTN_P_ID` | [RX_METHOD_RELTN](RX_METHOD_RELTN.md) | `RX_METHOD_RELTN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_METHOD_RELTN](RX_METHOD_RELTN.md) | `RX_METHOD_RELTN_P_ID` |

