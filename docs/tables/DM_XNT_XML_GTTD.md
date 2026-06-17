# DM_XNT_XML_GTTD

> Global Temporary Table used for Extract and Transform Archive process to store person related data to be extracted into an XML source.

**Description:** Data Management Extract and Transform XML Global Temporary Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `XML_SEQ` | DOUBLE |  |  | Used to order the output, contains value from DM_CLINICAL_SEQ. |
| 2 | `XML_STR` | VARCHAR(4000) |  |  | Used to store the XML output. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

