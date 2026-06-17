# OEN_PERSONALITY

> This table stores the personality traits for the open engine interface.

**Description:** open engine interface personality traits  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEF_ASYNC_IN` | DOUBLE |  |  | This column is for future use. |
| 2 | `DEF_ASYNC_OUT` | DOUBLE |  |  | This column is for future use. |
| 3 | `DEF_DISK_IN` | DOUBLE |  |  | This column is for future use. |
| 4 | `DEF_DISK_OUT` | DOUBLE |  |  | This column is for future use. |
| 5 | `DEF_GENERAL` | DOUBLE |  |  | This column is for future use. |
| 6 | `DEF_TCPIP_IN` | DOUBLE |  |  | This column is for future use. |
| 7 | `DEF_TCPIP_OUT` | DOUBLE |  |  | This column is for future use. |
| 8 | `HANDLED_BY_GUI` | DOUBLE | NOT NULL |  | This is the flag which determines if the trait could be handled by GUI or not. |
| 9 | `INTERFACEID` | DOUBLE | NOT NULL |  | This is the ID of the interface. |
| 10 | `NAME` | CHAR(32) |  |  | This column represents the trait name. |
| 11 | `PERSONALITY_KEY` | CHAR(40) | NOT NULL |  | This column represents the personality key which is the combination of interfaceid and trait name. |
| 12 | `VALUE` | VARCHAR(500) |  |  | This column represents the trait value. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

