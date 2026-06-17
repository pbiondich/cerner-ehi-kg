# RX_CURVE

> Stores properties of calcium phosphate curves.

**Description:** Rx Curve  
**Table type:** REFERENCE  
**Primary key:** `RX_CURVE_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AMINO_ACID_CONC_PCT` | DOUBLE | NOT NULL |  | The concentration of amino acid associated to the solubility curve, expressed as a percentage of weight to volume. |
| 2 | `CALCIUM_UNIT_CD` | DOUBLE | NOT NULL |  | Code value for the unit of measure used to express the curve's calcium values. |
| 3 | `CURVE_CD` | DOUBLE | NOT NULL |  | Code value for the curve. |
| 4 | `CYSTEINE_IND` | DOUBLE | NOT NULL |  | Indication that the curve is defined for user with orders that have cysteine. |
| 5 | `DEXTROSE_CONC_PCT` | DOUBLE | NOT NULL |  | The concentration of dextrose associated to the solubility curve, expressed as a percentage of weight to volume. |
| 6 | `PHOSPHATE_UNIT_CD` | DOUBLE | NOT NULL |  | Code value for the unit of measure used to express the curve's phosphate values. |
| 7 | `RX_CURVE_ID` | DOUBLE | NOT NULL | PK | Unique, generated primary key for the RX_CURVE table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_CURVE_MBR](RX_CURVE_MBR.md) | `RX_CURVE_ID` |

